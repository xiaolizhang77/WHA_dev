import cv
import tools
import adb
def returnHome():
    for i in range(10):
        if tools.match_pics() == "home":
            print("这是主页")
            return
        tools.back()
    raise Exception("Error")
