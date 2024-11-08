from PIL import Image
import os


def convert_images_to_png(source_folder, target_folder):
    # Ensure target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Supported file extensions
    supported_extensions = ('.webp', '.jpg', '.jpeg')

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(supported_extensions):
            # Define the full file path
            img_path = os.path.join(source_folder, filename)

            # Open the image file
            with Image.open(img_path) as img:
                # Remove the original file extension and add .png
                png_filename = os.path.splitext(filename)[0] + '.png'
                png_path = os.path.join(target_folder, png_filename)

                # Convert and save the image as .png
                img.save(png_path, 'PNG')
                print(f"Converted {filename} to {png_filename}")


# Usage
source_folder = './images/original'
target_folder = './images/converted'
convert_images_to_png(source_folder, target_folder)
