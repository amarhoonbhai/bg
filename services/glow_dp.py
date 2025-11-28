from io import BytesIO
from PIL import Image, ImageDraw, ImageFilter

def glow_dp(image_bytes: bytes) -> BytesIO:
    img = Image.open(BytesIO(image_bytes)).convert("RGBA")
    size = img.size[0]

    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    dp = img.copy()
    dp.putalpha(mask)

    glow = dp.filter(ImageFilter.GaussianBlur(40))

    combined = Image.alpha_composite(glow, dp)

    buf = BytesIO()
    combined.save(buf, format="PNG")
    buf.seek(0)
    return buf
