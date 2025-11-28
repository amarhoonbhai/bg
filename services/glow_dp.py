from io import BytesIO
from PIL import Image, ImageFilter, ImageOps


def glow_dp(image_bytes: bytes) -> BytesIO:
    img = Image.open(BytesIO(image_bytes)).convert("RGBA")

    # create circle mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

    # apply circular crop
    dp = ImageOps.fit(img, img.size)
    dp.putalpha(mask)

    # glow effect
    glow = dp.filter(ImageFilter.GaussianBlur(40))

    final = Image.alpha_composite(glow, dp)

    buf = BytesIO()
    final.save(buf, format="PNG")
    buf.seek(0)
    return buf
