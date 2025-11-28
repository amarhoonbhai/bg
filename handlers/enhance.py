from io import BytesIO
from PIL import Image
import numpy as np
import cv2
from skimage import restoration

def upscale_image(image_bytes: bytes) -> BytesIO:
    # Open image
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)

    # 2X upscale using OpenCV
    upscale = cv2.resize(img_np, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Light denoise using skimage
    denoise = restoration.denoise_bilateral(
        upscale,
        sigma_color=0.05,
        sigma_spatial=15,
        channel_axis=-1
    )

    denoise_uint8 = (denoise * 255).astype(np.uint8)

    final = Image.fromarray(denoise_uint8)

    buf = BytesIO()
    final.save(buf, format="PNG")
    buf.seek(0)

    return buf
