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


def sleepTime(n):
    time.sleep(n)


def match_pic(pic_name):
    print(f"match_pic:{pic_name}")
    current_image = cv.calculate_histogram(f"./pic/{pic_name}")
    b_score = 0
    b_name = ""
    for screen_name, known_screenshot_path in const.known_screenshot_paths.items():
        if screen_name in const.known_screenshot_area.keys():
            x, y, w, h = const.known_screenshot_area[screen_name]
            current_area = cv.calculate_area(f"./pic/{pic_name}", x, y, w, h)
            score = cv.compare_area(current_area, known_screenshot_path)
            if score > 0.95:
                print(f"area:{screen_name},score: {score}")
        else:
            score = cv.compare_histograms(current_image, known_screenshot_path)
            if score > 0.95:
                print(f"image:{screen_name},score: {score}")
        if score > b_score:
            b_score = score
            b_name = screen_name
    # 假设阈值为0.9，表示高度相似
    if b_score > 0.8:
        print(f"Current screen is: ${b_name}$, score: {b_score}")
        return b_name
    return "No match found"


def match_pics():
    name = get_pic_name()
    adb.get_screen_cut(name)
    return match_pic(name)


def match_button(pic: str, button: str):
    name = get_pic_name()
    adb.get_screen_cut(name)
    print(f"match_buttoning:{button}")
    if match_pic(name) == pic:
        x, y, w, h = const.button[button]
        current_area = cv.calculate_area(f"./pic/{name}", x, y, w, h)
        score = cv.compare_button(current_area, const.known_screenshot_paths[pic])
        print(f"button:{button},score:{score}")
        if score > 0.95:
            return True
        else:
            return False
    else:
        return False


def match_buttons(pic: str):
    return match_button(pic, pic)


def back():
    adb.perform_click(70, 50)
    sleep()


def press_hold(x, y, t):
    adb.press_and_hold(x, y, t * 1000)
