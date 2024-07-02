from datetime import datetime
import time
import cv
import const
def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_pic_name():
    return f"screenshot_{get_timestamp()}.png"

def sleep():
    time.sleep(1)

def match_pic(pic_name):
    current_image = cv.load_image(f"./pic/{pic_name}")
    for screen_name, known_screenshot_path in const.known_screenshot_paths.items():
        known_image = cv.load_image(known_screenshot_path)
        score = cv.compare_images(current_image, known_image)
        print(f"Similarity with {screen_name}: {score}")

        # 假设阈值为0.9，表示高度相似
        if score > 0.9:
            print(f"Current screen is: {screen_name}")
            return screen_name
    return None