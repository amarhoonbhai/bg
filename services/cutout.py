import cv2
import numpy as np
from PIL import Image
from io import BytesIO


def do_cutout(img_bytes: bytes):
    pil = Image.open(BytesIO(img_bytes)).convert("RGB")
    img = np.array(pil)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 180)

    conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not conts:
        return BytesIO(img_bytes)

    c = max(conts, key=cv2.contourArea)
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)

    cut = cv2.bitwise_and(img, img, mask=mask)
    final = Image.fromarray(cut)

    buf = BytesIO()
    final.save(buf, format="PNG")
    buf.seek(0)
    return buf
