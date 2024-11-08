from PIL import Image
import os


def convert_images(source_folder, target_folder, extension):
    # Ensure the target extension is valid
    if not extension.startswith('.'):
        extension = '.' + extension
    extension = extension.lower()

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        # Full file path
        img_path = os.path.join(source_folder, filename)

        # Try to open and process the image
        try:
            with Image.open(img_path) as img:
                # Remove the original file extension and add the target extension
                target_filename = os.path.splitext(filename)[0] + extension
                target_path = os.path.join(target_folder, target_filename)

                # Convert and save the image in the target format
                img.save(target_path)
                print(f"Converted {filename} to {target_filename}")

        except Exception as e:
            print(f"Skipping {filename}: {e}")


# Usage
source_folder = './images/original'
target_folder = './images/converted'
target_extension = 'png'  # Change this to your desired target extension (e.g., 'png', 'jpeg', 'bmp', etc.)
convert_images(source_folder, target_folder, target_extension)