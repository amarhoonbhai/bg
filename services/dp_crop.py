from io import BytesIO
from PIL import Image
import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def auto_crop_dp(image_bytes: bytes) -> BytesIO:
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)

    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        # fallback: center crop
        h, w = img_np.shape[:2]
        size = min(h, w)
        crop = img_np[h//2 - size//2:h//2 + size//2, w//2 - size//2:w//2 + size//2]
    else:
        x, y, w, h = faces[0]
        cx = x + w//2
        cy = y + h//2
        r = max(w, h) // 1

        crop = img_np[cy-r:cy+r, cx-r:cx+r]

    resized = cv2.resize(crop, (800, 800))  # DP perfect size
    output = Image.fromarray(resized)

    buf = BytesIO()
    output.save(buf, format="PNG")
    buf.seek(0)
    return buf
