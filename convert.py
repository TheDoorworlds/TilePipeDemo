from colors import TRANSPILE
from uuid import uuid4
from PIL import Image
from pathlib import PurePosixPath, Path

# Define a list of color replacement dictionaries using hex colors
def hex_to_rgba(hex_color):
    """Convert hex color to RGBA tuple."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    elif len(hex_color) == 8:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
    else:
        raise ValueError(f"Invalid hex color: {hex_color}")

def replace_colors(filename, color_replacement_hex):
    # Extract and remove the filename from the dictionary
    color_replacement_hex.pop('filename')
    
    # Convert hex colors to RGBA
    color_replacement = {hex_to_rgba(k): hex_to_rgba(v) if v != 'transparent' else (0, 0, 0, 0) for k, v in color_replacement_hex.items()}
    
    # Open the image
    img = Image.open(PurePosixPath(Path(__file__).resolve().parent, 'ConverterInput.png').as_posix())
    img = img.convert("RGBA")
    
    # Load pixel data
    pixels = img.load()
    
    # Iterate through each pixel
    for y in range(img.height):
        for x in range(img.width):
            current_color = pixels[x, y]
            if current_color in color_replacement:
                pixels[x, y] = color_replacement[current_color]
    
    # Check for output folder
    output_path = PurePosixPath(Path(__file__).resolve().parent, 'output').as_posix()
    Path(output_path).mkdir(exist_ok=True)

    # Save the modified image
    img.save(PurePosixPath(output_path, filename).as_posix())

    # Restore the filename to the dictionary for further use
    color_replacement_hex['filename'] = filename

# Process each color replacement dictionary
for color_replacement_hex in TRANSPILE:
    filename_no_extention = color_replacement_hex.get('filename', 'default')
    if filename_no_extention == 'default':
        filename = f'{uuid4()}.png'
    else:
        filename = f'{filename_no_extention}.png'
    replace_colors(filename, color_replacement_hex)
