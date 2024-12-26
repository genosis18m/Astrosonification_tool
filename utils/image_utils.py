import numpy as np
from PIL import Image

def npy_to_image(npy_file, image_file):
    data = np.load(npy_file)
    # Normalize data to 0-255 for RGB conversion
    normalized_data = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)
    # Convert grayscale to RGB
    rgb_data = np.stack([normalized_data]*3, axis=-1)
    image = Image.fromarray(rgb_data)
    image.save(image_file)
