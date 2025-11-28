from io import BytesIO
from PIL import Image
import numpy as np
import cv2


def restore_face(image_bytes: bytes) -> BytesIO:
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)

    # Light denoise
    denoise = cv2.fastNlMeansDenoisingColored(img_np, None, 10, 10, 7, 21)

    # Sharpen
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(denoise, -1, kernel)

    final = Image.fromarray(sharp)

    buf = BytesIO()
    final.save(buf, format="PNG")
    buf.seek(0)
    return buf
