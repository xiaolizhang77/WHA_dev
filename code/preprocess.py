import cv
import const
import os
import pickle
# 输出特征文件路径
output_file = "./known_features.pkl"
# 预处理图像并保存特征
converted_dict = {v for k, v in const.known_screenshot_paths.items()}
cv.save_feature_data(converted_dict, output_file)
print(f"Features saved to {output_file}")

output_file2 = "./known_features_area.pkl"
features = {}
for k, v in const.known_screenshot_area.items():
    print(f"{k}:{v}")
    image_path = const.known_screenshot_paths.get(k)
    features[os.path.basename(image_path)] = cv.calculate_area(image_path, v[0], v[1], v[2], v[3])
with open(output_file2, 'wb') as f:
    pickle.dump(features, f)
