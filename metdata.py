from PIL import Image
from PIL.ExifTags import TAGS

image_path = r"C:\Users\konda\OneDrive\Desktop\new pic prodfessional.jpeg"
try:
    image = Image.open(image_path)

    print("\n----- Basic Metadata -----")
    print(f"Filename : {image.filename}")
    print(f"Format   : {image.format}")
    print(f"Mode     : {image.mode}")
    print(f"Size     : {image.size}")

    print("\n----- EXIF Metadata -----")
    exif_data = image.getexif()

    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
    else:
        print("No EXIF metadata found.")

except Exception as e:
    print("Error:", e)