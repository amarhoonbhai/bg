from io import BytesIO
from PIL import Image
import numpy as np
from gfpgan import GFPGANer


gfpganer = GFPGANer(
    model_path='GFPGANv1.4.pth',
    upscale=2,
    arch='clean',
    channel_multiplier=2
)


def restore_face(image_bytes: bytes) -> BytesIO:
    img = np.array(Image.open(BytesIO(image_bytes)).convert("RGB"))

    _, _, restored = gfpganer.enhance(img, has_aligned=False, only_center_face=False)

    restored_img = Image.fromarray(restored)

    buf = BytesIO()
    restored_img.save(buf, format="PNG")
    buf.seek(0)
    return buf
