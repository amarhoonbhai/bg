from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from skimage import restoration

def upscale_image(image_bytes: bytes) -> BytesIO:
    # Load image
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)

    # 2x upscale using OpenCV
    upscaled = cv2.resize(img_np, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Light bilateral denoise
    denoised = restoration.denoise_bilateral(
        upscaled,
        sigma_color=0.05,
        sigma_spatial=15,
        channel_axis=-1
    )

    denoised_uint8 = (denoised * 255).astype(np.uint8)

    final_image = Image.fromarray(denoised_uint8)

    buf = BytesIO()
    final_image.save(buf, format="PNG")
    buf.seek(0)

    return buf
