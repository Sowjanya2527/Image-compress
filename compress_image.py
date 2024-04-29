from PIL import Image
import os
 
def compress_image(input_path, output_path, quality=85):

    try:

        img = Image.open(input_path)

        img.save(output_path, quality=quality, optimize=True)
        print("Image compression successful!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
        input_image = "input_image.jpg"
        output_image = "compressed_image.jpg"
        compress_image(input_image, output_image)
