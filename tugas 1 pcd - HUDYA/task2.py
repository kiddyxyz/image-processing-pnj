from PIL import Image
import numpy as np

data = np.zeros((100, 100, 3), dtype=np.uint8)
for x in range(100): data[x, 14] = [255, 255, 255]
img = Image.fromarray(data, 'RGB')
img.save('garis.png')