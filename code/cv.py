import cv2
import pickle
import os

known_features = {}
known_features_areas = {}


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


def calculate_area(image_path, x, y, w, h):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return None
    image = image[y:y + h, x:x + w]
    # cv2.imshow("ROI", image)
    # cv2.waitKey(0)
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()


def compare_histograms(hist1, hist2_path):
    hist2 = known_features[os.path.basename(hist2_path)]
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)


def compare_area(hist1, hist2_path):
    hist2 = known_features_areas[os.path.basename(hist2_path)]
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
    if not os.path.exists("./known_features.pkl"):
        print(f"File not found: ./known_features.pkl")
    with open("./known_features.pkl", 'rb') as f:
        known_features = pickle.load(f)
    global known_features_areas
    if not os.path.exists("./known_features_area.pkl"):
        print(f"File not found: ./known_features_area.pkl")
    with open("./known_features_area.pkl", 'rb') as f2:
        known_features_areas = pickle.load(f2)
