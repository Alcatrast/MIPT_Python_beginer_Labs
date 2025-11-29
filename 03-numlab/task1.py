from PIL import Image
import numpy as np

file_path = r"lunar_images\lunar"
for i in range(1, 4):
    img = Image.open(f"{file_path}0{i}_raw.jpg")
    data = np.array(img)
    min_val = data.min()
    max_val = data.max()
    k = 255.0 / (max_val - min_val)
    data = (data - min_val) * k
    data = data.astype(np.uint8)
    result_img = Image.fromarray(data)
    result_img.save(f"{file_path}0{i}_enhanced.jpg")