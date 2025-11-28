import cv2
import numpy as np
from PIL import Image
from io import BytesIO


def do_cutout(image_bytes: bytes) -> BytesIO:
    """
    Cut-out using OpenCV contour extraction.
    """
    try:
        # load PIL
        pil = Image.open(BytesIO(image_bytes)).convert("RGB")
        img = np.array(pil)

        # grayscale + edge detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 70, 150)

        # find contours
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not conts:
            # fallback = return original
            buf = BytesIO(image_bytes)
            buf.seek(0)
            return buf

        # largest contour
        c = max(conts, key=cv2.contourArea)

        # make mask
        mask = np.zeros(gray.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        # apply mask
        cut = cv2.bitwise_and(img, img, mask=mask)

        # save result
        result = Image.fromarray(cut)
        buf = BytesIO()
        result.save(buf, format="PNG")
        buf.seek(0)
        return buf

    except Exception as e:
        print("Cut-out error:", e)
        buf = BytesIO(image_bytes)
        buf.seek(0)
        return buf
