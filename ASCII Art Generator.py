import numpy as np
from PIL import Image as im
from PIL import ImageEnhance, ImageFilter
import os
from pathlib import Path
import requests
from io import BytesIO

ascii_list = [ ' ', '.', ':', '-', '=', '+', '*', '#', '%', '@' ]
length = len(ascii_list)

def download_image_from_url(url):
    """
    Downloads an image from the given URL.

    Parameters
    ----------
    url : str
        The URL of the image to download.

    Returns
    -------
    PIL.Image
        The downloaded image as a PIL Image object.
    """
    response = requests.get(url)
    return im.open(BytesIO(response.content))

def get_file_name(path):
    # Get the file name with extension
    full_file_name = os.path.basename(path)
    # Split the file name and extension
    file_name, file_extension = os.path.splitext(full_file_name)
    return file_name



palette = [
    (0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0),
    (0, 0, 128), (128, 0, 128), (0, 128, 128), (192, 192, 192),
    (128, 128, 128), (255, 0, 0), (0, 255, 0), (255, 255, 0),
    (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255),
    (0, 0, 0), (0, 0, 95), (0, 0, 135), (0, 0, 175),
    (0, 0, 215), (0, 0, 255), (0, 95, 0), (0, 95, 95),
    (0, 95, 135), (0, 95, 175), (0, 95, 215), (0, 95, 255),
    (0, 135, 0), (0, 135, 95), (0, 135, 135), (0, 135, 175),
    (0, 135, 215), (0, 135, 255), (0, 175, 0), (0, 175, 95),
    (0, 175, 135), (0, 175, 175), (0, 175, 215), (0, 175, 255),
    (0, 215, 0), (0, 215, 95), (0, 215, 135), (0, 215, 175),
    (0, 215, 215), (0, 215, 255), (0, 255, 0), (0, 255, 95),
    (0, 255, 135), (0, 255, 175), (0, 255, 215), (0, 255, 255),
    (95, 0, 0), (95, 0, 95), (95, 0, 135), (95, 0, 175),
    (95, 0, 215), (95, 0, 255), (95, 95, 0), (95, 95, 95),
    (95, 95, 135), (95, 95, 175), (95, 95, 215), (95, 95, 255),
    (95, 135, 0), (95, 135, 95), (95, 135, 135), (95, 135, 175),
    (95, 135, 215), (95, 135, 255), (95, 175, 0), (95, 175, 95),
    (95, 175, 135), (95, 175, 175), (95, 175, 215), (95, 175, 255),
    (95, 215, 0), (95, 215, 95), (95, 215, 135), (95, 215, 175),
    (95, 215, 215), (95, 215, 255), (95, 255, 0), (95, 255, 95),
    (95, 255, 135), (95, 255, 175), (95, 255, 215), (95, 255, 255),
    (135, 0, 0), (135, 0, 95), (135, 0, 135), (135, 0, 175),
    (135, 0, 215), (135, 0, 255), (135, 95, 0), (135, 95, 95),
    (135, 95, 135), (135, 95, 175), (135, 95, 215), (135, 95, 255),
    (135, 135, 0), (135, 135, 95), (135, 135, 135), (135, 135, 175),
    (135, 135, 215), (135, 135, 255), (135, 175, 0), (135, 175, 95),
    (135, 175, 135), (135, 175, 175), (135, 175, 215), (135, 175, 255),
    (135, 215, 0), (135, 215, 95), (135, 215, 135), (135, 215, 175),
    (135, 215, 215), (135, 215, 255), (135, 255, 0), (135, 255, 95),
    (135, 255, 135), (135, 255, 175), (135, 255, 215), (135, 255, 255),
    (175, 0, 0), (175, 0, 95), (175, 0, 135), (175, 0, 175),
    (175, 0, 215), (175, 0, 255), (175, 95, 0), (175, 95, 95),
    (175, 95, 135), (175, 95, 175), (175, 95, 215), (175, 95, 255),
    (175, 135, 0), (175, 135, 95), (175, 135, 135), (175, 135, 175),
    (175, 135, 215), (175, 135, 255), (175, 175, 0), (175, 175, 95),
    (175, 175, 135), (175, 175, 175), (175, 175, 215), (175, 175, 255),
    (175, 215, 0), (175, 215, 95), (175, 215, 135), (175, 215, 175),
    (175, 215, 215), (175, 215, 255), (175, 255, 0), (175, 255, 95),
    (175, 255, 135), (175, 255, 175), (175, 255, 215), (175, 255, 255),
    (215, 0, 0), (215, 0, 95), (215, 0, 135), (215, 0, 175),
    (215, 0, 215), (215, 0, 255), (215, 95, 0), (215, 95, 95),
    (215, 95, 135), (215, 95, 175), (215, 95, 215), (215, 95, 255),
    (215, 135, 0), (215, 135, 95), (215, 135, 135), (215, 135, 175),
    (215, 135, 215), (215, 135, 255), (215, 175, 0), (215, 175, 95),
    (215, 175, 135), (215, 175, 175), (215, 175, 215), (215, 175, 255),
    (215, 215, 0), (215, 215, 95), (215, 215, 135), (215, 215, 175),
    (215, 215, 215), (215, 215, 255), (215, 255, 0), (215, 255, 95),
    (215, 255, 135), (215, 255, 175), (215, 255, 215), (215, 255, 255),
    (255, 0, 0), (255, 0, 95), (255, 0, 135), (255, 0, 175),
    (255, 0, 215), (255, 0, 255), (255, 95, 0), (255, 95, 95),
    (255, 95, 135), (255, 95, 175), (255, 95, 215), (255, 95, 255),
    (255, 135, 0), (255, 135, 95), (255, 135, 135), (255, 135, 175),
    (255, 135, 215), (255, 135, 255), (255, 175, 0), (255, 175, 95),
    (255, 175, 135), (255, 175, 175), (255, 175, 215), (255, 175, 255),
    (255, 215, 0), (255, 215, 95), (255, 215, 135), (255, 215, 175),
    (255, 215, 215), (255, 215, 255), (255, 255, 0), (255, 255, 95),
    (255, 255, 135), (255, 255, 175), (255, 255, 215), (255, 255, 255),
    (8, 8, 8), (18, 18, 18), (28, 28, 28), (38, 38, 38),
    (48, 48, 48), (58, 58, 58), (68, 68, 68), (78, 78, 78),
    (88, 88, 88), (98, 98, 98), (108, 108, 108), (118, 118, 118),
    (128, 128, 128), (138, 138, 138), (148, 148, 148), (158, 158, 158),
    (168, 168, 168), (178, 178, 178), (188, 188, 188), (198, 198, 198),
    (208, 208, 208), (218, 218, 218), (228, 228, 228), (238, 238, 238)
]

n_colors, _ = np.array(palette).shape


# n is the reduction factor
def image_processing(img, n, contrast_factor=1.5, sharpness_factor=2.0, brightness_factor=1.2):
        
    # img = im.open(img_path)  
  
    w, h = img.size
    img = img.resize(((int(w/n)), int((h * 0.6)/n)) , im.LANCZOS)  
    
    # Enhance brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness_factor)

    # Enhance contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast_factor)
    
    # Sharpen image
    img = img.filter(ImageFilter.SHARPEN)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness_factor)
    
    gray = img.convert('L')

    # # Check if the image has 4 channels
    # if img.mode != 'RGBA':
    #     raise ValueError("Image must have 4 color channels (RGBA mode).")

    # # Convert to RGB mode, discarding the alpha channel
    # img = img.convert('RGB')
    
    img_array = np.array(img)
    gray_array = np.array(gray)         
    
    return gray_array , img_array 


def gray_ascii(gray_array):   
    
    #creating intensity array from grayscale image array
    gray_array = ((gray_array - gray_array.min()) / (gray_array.max() - gray_array.min())) * (length - 1) 
    
    mask1 = (gray_array - np.floor(gray_array)) >= 0.5
    
    intensity_array = np.where(mask1, np.ceil(gray_array), np.floor(gray_array)).astype(int)    
    
    #using intensity array for grayscale ASCII Art
    gray_art = ''
    
    h, w = intensity_array.shape
    
    for i, c in enumerate(intensity_array.flatten()):
        
        if (i+1) % w == 0 :
            gray_art += ascii_list[c] + '\n'
        else :
            gray_art += ascii_list[c]       
        
    return gray_art


def nearest_color_array(img_array, palette, weights=(0.3, 0.59, 0.11)):
    
    h, w, _ = img_array.shape
    
    w_img = ( img_array / 25.5 ) * np.array(weights)  
    w_palette = ( np.array(palette)  / 25.5 ) * np.array(weights)
    
    #While carrying out multi dimensional operations in Image Processing it is better to keep color channel as the last dim
    w_img = w_img.reshape(h, w, 1, 3)
    w_palette = w_palette.reshape(1, 1, n_colors, 3)
    
    distance = np.linalg.norm((w_img - w_palette), axis=3)
    
    return np.argmin(distance, axis = 2)


def color_ascii(gray_art, nearest_color_arr):
    
    color_art = ''
    
    h, w = nearest_color_arr.shape
    
    l = nearest_color_arr.flatten()
    
    for i, c in enumerate(list(gray_art.replace("\n", ""))):
        
        if (i+1) % w == 0:            
            color_art += f"\033[38;5;{l[i]}m{c}\n\033[0m"
        else :
            color_art += f"\033[38;5;{l[i]}m{c}\033[0m"              
    
    return color_art


def gray_ascii_Generator_from_URL(url, reduction_factor = 2):

    """
    Generates a grayscale ASCII art from the given image file and saves it to a file in the same directory.

    Parameters
    ----------
    url : str
        The path to the image file.
    reduction_factor : int, optional
        The reduction factor for the image size. Defaults to 2.

    Returns
    -------
    str
        The path to the generated ASCII art file.

    """
    
    rf = reduction_factor

    img = download_image_from_url(url)
    file_name = url.split('/')[-1].split('.')[0]  # Extract filename from URL

    gray_arr, _ = image_processing(img, rf)

    gray_art = gray_ascii(gray_arr)

    # Construct the save path using pathlib (this is OS-independent)
    save_dir = Path(file_path).parent / "ASCII Art" / "GrayScale"
    save_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    save_path = save_dir / f"{file_name} Gray.txt"
    
    with save_path.open('w') as file:
        file.write(gray_art)

    return str(save_path)

def color_ascii_Generator_from_URL(url, reduction_factor = 2):

    """
    Generates a color ASCII art from the given image file and saves it to a file in the same directory.

    Parameters
    ----------
    url : str
        The path to the image file.
    reduction_factor : int, optional
        The reduction factor for the image size. Defaults to 2.

    Returns
    -------
    str
        The path to the generated ASCII art file.

    """
    rf = reduction_factor

    img = download_image_from_url(url)
    file_name = url.split('/')[-1].split('.')[0]  # Extract filename from URL

    gray_arr, img_arr = image_processing(img, rf)

    nearest_color_arr = nearest_color_array(img_arr, palette)

    gray_art = gray_ascii(gray_arr)

    color_art = color_ascii(gray_art, nearest_color_arr)

    # Construct the save path using pathlib (this is OS-independent)
    save_dir = Path(file_path).parent / "ASCII Art" / "Color"
    save_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    save_path = save_dir / f"{file_name} Color_ASCII.txt"
    
    with save_path.open('w') as file:
        file.write(color_art)

    return str(save_path)







