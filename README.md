
# Image Format Converter

A Python script to convert images from any format to a specified target format using the `Pillow` library. This script automatically processes all images in a source folder and saves them in the specified format in a target folder.

## Requirements

- Python 3.x
- `Pillow` library

Install the `Pillow` library if you haven’t already:

```bash
pip install pillow
```

## Usage

1. **Set up folders:**
   - Define the `source_folder` as the path to the folder containing the original images.
   - Define the `target_folder` as the path where the converted images will be saved.

2. **Choose the target format:**
   - Set `target_extension` to your desired file extension (e.g., `png`, `jpeg`, `bmp`).

3. **Run the Script:**

   Update the paths and target extension, then run the script to convert images:

   ```python
   source_folder = './images/original'
   target_folder = './images/converted'
   target_extension = 'png'  # Set your target format here

   convert_images(source_folder, target_folder, target_extension)
   ```

### Example

The following example converts all images in the `./images/original` folder to PNG format and saves them in the `./images/converted` folder:

```python
source_folder = './images/original'
target_folder = './images/converted'
target_extension = 'png'
convert_images(source_folder, target_folder, target_extension)
```

## Function Details

- `convert_images(source_folder, target_folder, extension)`: Converts images in the `source_folder` to the specified `extension` format and saves them in `target_folder`.

### Error Handling

The script skips unsupported or corrupted files and displays an error message without interrupting the conversion of other files.

## License

This script is provided as-is and can be modified and distributed freely.
