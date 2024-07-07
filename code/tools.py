from datetime import datetime
import time
import cv
import const
import os
import glob
import adb

def delete_png_files():
    directory = const.directory
    # 构建要删除的文件路径模式
    file_pattern = os.path.join(directory, "*.png")
    # 查找所有匹配的文件
    files = glob.glob(file_pattern)
    # 遍历并删除所有匹配的文件
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_pic_name():
    return f"screenshot_{get_timestamp()}.png"

def sleep():
    time.sleep(3)

def match_pic(pic_name):
    current_image = cv.calculate_histogram(f"./pic/{pic_name}")
    b_score = 0
    b_name = ""
    for screen_name, known_screenshot_path in const.known_screenshot_paths.items():
        score = cv.compare_histograms(current_image,known_screenshot_path)
        if score > b_score:
            b_score = score
            b_name = screen_name
        # print(f"Similarity with {screen_name}: {score}")
    # 假设阈值为0.9，表示高度相似
    if b_score > 0.7:
        print(f"Current screen is: ${b_name}$, score: {b_score}")
        return b_name
    return "No match found"

def match_pics():
    name = get_pic_name()
    adb.get_screen_cut(name)
    return match_pic(name)

def back():
    adb.perform_click(70, 50)
    sleep()