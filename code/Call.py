import home
import adb
import tools


def enterCall():
    for i in range(5):
        str = tools.match_pics()
        if str == "callMain" or str == "confirmCall0" or str == "confirmCall1":
            return str
        try:
            home.returnHome()
        except Exception as e:
            raise e
        adb.perform_click(1500, 850)
        tools.sleep()
    raise Exception("Enter Call Error")


def confirmCall():
    adb.perform_click(1650, 950)
    tools.sleep()
    for i in range(5):
        if tools.match_pics() == "confirmCall2":
            tools.press_hold(1000, 500, 3)
        elif i == 5:
            raise Exception("Call Error")
    for i in range(10):
        if tools.match_pics() == "confirmCall3" or tools.match_pics() == "confirmCall4" or tools.match_pics() == "confirmCall5" or tools.match_pics() == "confirmCall6" or tools.match_pics() == "confirmCall7":
            adb.perform_click(1870, 50)
            tools.sleep()
        else:
            break
    if tools.match_pics() == "callEnd" or tools.match_pics() == "callEnd2":
        tools.sleep()
        adb.perform_click(950, 930)
        tools.sleep()
    else:
        raise Exception("Call Error")


def callNew():
    e = 0
    for i in range(5):
        try:
            str = enterCall()
        except Exception as e:
            raise e
        if str == "callMain":
            e = 1
            break
        adb.perform_click(475, 543)
        tools.sleep()
    if e == 0:
        raise Exception("Call New Error")
    adb.perform_click(1650, 950)
    tools.sleep()
    if tools.match_pics() == "callNum":
        adb.perform_click(1150, 520)
        tools.sleepTime(1)
    elif tools.match_pics() == "callMain":
        print("征集信不足")
        return
    else:
        raise Exception("Call New Error")
    if tools.match_pics() == "callNum":
        adb.perform_click(1130, 650)
        tools.sleepTime(1)
    else:
        raise Exception("Call New Error")
    return


def call():
    try:
        str = enterCall()
    except Exception as e:
        raise e
    if str == "callMain":
        callNew()
    else:
        confirmCall()
        callNew()
    try:
        home.returnHome()
    except Exception as e:
        raise e
    tools.delete_png_files()
