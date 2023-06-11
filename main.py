from PIL import Image
from pillow_heif import register_heif_opener
import os

help(register_heif_opener)

dir_source = '...'
output_source = '...'
list_files = os.listdir(dir_source)

heic_files = [f for f in list_files if f.endswith('.heic')]

print("Number of files: ", len(heic_files))

register_heif_opener()

convert_to = ".png"
for photo in heic_files:
    img = Image.open(os.path.join(dir_source, photo))
    img.save(os.path.join(output_source, photo.replace('.heic', convert_to)))
    print("Saved: ", photo.replace('.heic', convert_to))