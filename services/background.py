from io import BytesIO
from rembg import remove

def remove_background(img_bytes):
    output = remove(img_bytes)
    buf = BytesIO(output)
    buf.seek(0)
    return buf
