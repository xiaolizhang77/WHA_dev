from skimage.metrics import structural_similarity as compare_ssim
import cv2
import pickle
import os

known_features = {}

def load_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

def calculate_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return None
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()

def compare_histograms(hist1, hist2_path):
    hist2 = known_features[os.path.basename(hist2_path)]
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def save_feature_data(image_paths, output_file):
    features = {}
    for image_path in image_paths:
        print(image_path)
        features[os.path.basename(image_path)] = calculate_histogram(image_path)
    with open(output_file, 'wb') as f:
        pickle.dump(features, f)

def load_feature_data():
    global known_features
    with open("./known_features.pkl", 'rb') as f:
        known_features = pickle.load(f)