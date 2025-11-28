from io import BytesIO
import cv2
import numpy as np
from PIL import Image
from realesrgan import RealESRGAN

model_loaded = None

def load_model():
    global model_loaded
    if model_loaded is None:
        from realesrgan import RealESRGAN
        import torch
        device = 'cpu'
        model_loaded = RealESRGAN(device, scale=4)
        model_loaded.load_weights('RealESRGAN_x4.pth', download=True)
    return model_loaded


def upscale_image(image_bytes: bytes) -> BytesIO:
    model = load_model()

    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)

    upscaled = model.predict(img_np)
    upscaled_img = Image.fromarray(upscaled)

    buf = BytesIO()
    upscaled_img.save(buf, format='PNG')
    buf.seek(0)
    return buf
