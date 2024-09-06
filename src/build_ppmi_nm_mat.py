import ants
import glob
from tqdm import tqdm  # For the progress bar

def load_images_to_matrix( image_filenames, mask ):
    """
    Load a list of images from a given set of filenames, crop them, and convert them to a matrix.
    
    Parameters:
    - image_filenames: list of str
        List of image file paths to load and process.
    - mask: ants.ANTsImage
        A mask image specifying the region of interest.
    
    Returns:
    - image_matrix: np.ndarray
        A 2D matrix where each column is a flattened image.
    """
    
    # Ensure we have image files to process
    if len(image_filenames) == 0:
        raise ValueError(f"No image files provided in the list.")
    
    # Step 1: Initialize an empty list to store the cropped images
    cropped_images = []
    
    # Step 2: Loop through the filenames, load, and crop each image
    for img_file in tqdm(image_filenames, desc="Processing images"):
        # Load the image using ANTsPy
        img = ants.image_read(img_file)
        
        # Crop the image (automatically crops to the non-zero region)
        cropped_img = ants.crop_image(img, mask )
        
        # Append the cropped image to the list
        cropped_images.append(cropped_img)
    
    # Step 3: Convert the list of cropped images to a matrix
    if not isinstance(mask, ants.ANTsImage):
        raise ValueError("The provided mask must be an ants.ANTsImage object.")
    image_matrix = ants.image_list_to_matrix(cropped_images, ants.crop_image(mask,mask) )
    return image_matrix


# Define the list of image filenames
image_filenames = glob.glob("processedCSVSRFIRST/PPMI/*/*/NM2DMT/*/PPMI-*-NM_norm.nii.gz")

# Optional: Define the mask (can be None if not using a mask)
mask_image = ants.image_read("~/.antspymm/PPMI_NM_template_mask.nii.gz")

# Load images and convert to matrix
image_matrix = load_images_to_matrix(image_filenames, mask=mask_image)
print("Image matrix shape:", image_matrix.shape)
