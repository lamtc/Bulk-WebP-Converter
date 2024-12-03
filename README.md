# Bulk WebP Converter

A simple and efficient tool to convert multiple images to WebP format while maintaining quality.

## Features

- Bulk conversion of images to WebP format
- Quality control slider (1-100)
- Optional prefix naming for converted images
- Progress bar for conversion tracking
- Support for PNG and JPEG input formats
- User-friendly GUI interface
- High-quality compression using Pillow's WebP encoder

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python webp_converter.py
```

2. Select the source folder containing your images
3. Choose the destination folder for the converted WebP images
4. (Optional) Enter a prefix and check "Apply prefix to all images" to rename all converted images
   - If enabled, images will be named as: prefix_1.webp, prefix_2.webp, etc.
   - If disabled, original filenames will be preserved
5. Adjust the quality slider (80 is recommended for a good balance)
6. Click "Convert to WebP" to start the conversion

## Supported Input Formats

- PNG (.png, .PNG)
- JPEG (.jpg, .jpeg, .JPG, .JPEG)

## Notes

- Higher quality settings will result in larger file sizes
- The tool uses Pillow's WebP encoder with method 6 for best compression
- Progress bar shows real-time conversion progress
- The application will notify you when the conversion is complete
