import ants
import glob
from tqdm import tqdm  # For the progress bar

def load_images_to_list( image_filenames, mask ):
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

    return cropped_images
    
import ants

def normalize_images_by_mean(image_list):
    """
    Normalize each ANTsImage in the list by dividing each image by its mean value.
    
    Parameters:
    - image_list: list of ants.ANTsImage
        A list of ANTsImage objects to normalize.
    
    Returns:
    - normalized_images: list of ants.ANTsImage
        A list of normalized ANTsImage objects.
    """
    normalized_images = []

    for img in tqdm(image_list, desc="normalizing images"):
        # Compute the mean of the image
        img_mean = img.mean()
        
        if img_mean == 0:
            continue
        
        # Divide the image by its mean
        normalized_img = img / img_mean
        
        # Append the normalized image to the list
        normalized_images.append(normalized_img)
    
    return normalized_images
   

# Define the list of image filenames
image_filenames = glob.glob("processedCSVSRFIRST/PPMI/*/*/NM2DMT/*/PPMI-*-NM_norm.nii.gz")

# Optional: Define the mask (can be None if not using a mask)
mask_image = ants.image_read("~/.antspymm/PPMI_NM_template_mask.nii.gz")

# Load images and convert to matrix
image_list = load_images_to_list(image_filenames, mask=mask_image)

maskc = ants.crop_image(mask_image,mask_image)

image_matrix = ants.image_list_to_matrix( image_list, maskc )

print("Image matrix shape:", image_matrix.shape)

ants.image_write( ants.from_numpy(image_matrix), '/tmp/ppmi_NM_matrix.mha' )
ants.image_write( maskc, '/tmp/ppmi_NM_matrix_mask.mha' )
ants.image_write( ants.merge_channels(image_list), '/tmp/ppmi_NM_multichannel.mha' )

ants.image_write( ants.merge_channels( normalize_images_by_mean(image_list) ), '/tmp/ppmi_NM_norm_multichannel.mha' )


