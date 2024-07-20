from rembg import remove
from PIL import Image
image_input = Image.open(r"image_path")
output = remove(image_input)
output.save(r"image_output")
