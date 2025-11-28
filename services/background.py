from rembg import remove
from io import BytesIO

def remove_background(image_bytes: bytes) -> BytesIO:
    output = remove(image_bytes)
    return BytesIO(output)
