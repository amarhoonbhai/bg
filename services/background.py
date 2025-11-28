from rembg import remove
from io import BytesIO


def remove_background(image_bytes: bytes) -> BytesIO:
    """
    Removes background from an image using rembg.
    """
    try:
        output = remove(image_bytes)
        buf = BytesIO(output)
        buf.seek(0)
        return buf
    except Exception as e:
        print("Error in BG removal:", e)
        return None
