import cv
import const
# 输出特征文件路径
output_file = "./known_features.pkl"
# 预处理图像并保存特征
converted_dict = {v for k, v in const.known_screenshot_paths.items()}
cv.save_feature_data(converted_dict, output_file)
print(f"Features saved to {output_file}")