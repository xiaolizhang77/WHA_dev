from skimage.metrics import structural_similarity as compare_ssim
import cv2

def load_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def compare_images(image1, image2):
    # Compute the Structural Similarity Index (SSI) between the two images
    if image1.shape == image2.shape:
        score, diff = compare_ssim(image1, image2, full=True)
        return score
    return -1