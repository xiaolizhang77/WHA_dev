import home
import adb
import tools


def enterDC():
    for i in range(5):
        if tools.match_pics() == "dispatchCompany":
            print("进入派遣公司")
            return
        try:
            home.returnHome()
        except Exception as e:
            raise e
        adb.perform_click(1750, 740)
        tools.sleep()
    raise Exception("Enter DC Error")


def getResourse():
    try:
        enterDC()
    except Exception as e:
        raise e
    adb.perform_click(1760, 970)
    tools.sleep()
    adb.perform_click(1760, 970)
    tools.sleep()

    try:
        enterDC()
    except Exception as e:
        raise e
    adb.perform_click(1500, 970)
    tools.sleep()
    adb.perform_click(1500, 970)
    tools.sleep()

    try:
        enterDC()
    except Exception as e:
        raise e
    adb.perform_click(832, 932)
    tools.sleep()
    adb.perform_click(400, 300)
    tools.sleep()
    print("获取资源")


def enterOffice():
    for i in range(5):
        if tools.match_pics() == "office":
            print("进入办公室")
            return
        try:
            enterDC()
        except Exception as e:
            raise e
        adb.perform_click(735, 285)
        tools.sleep()
    raise Exception("Enter Office Error")


def drinkTea():
    print("喝不了一点")


def capsuleToy():
    try:
        enterOffice()
    except Exception as e:
        raise e
    adb.perform_click(335, 135)
    tools.sleep()
    if tools.match_pics() == "machine":
        adb.perform_click(1365, 575)
        tools.sleep()
        adb.perform_click(1365, 575)
        tools.sleep()
        print("开扭")
    elif tools.match_pics() == "office":
        print("扭过了")
    print("扭蛋机完成")
    tools.back()


def addBookItem():
    for i in range(3):
        try:
            enterDC()
        except Exception as e:
            raise e
        adb.perform_click(150, 650)
        tools.sleep()
        if tools.match_pics() == "book":
            adb.perform_click(400, 850)
            tools.sleep()
            adb.perform_click(1600, 820)
            tools.sleep()
            adb.perform_click(1500, 970)
            tools.sleep()
            str = tools.match_pics()
            if str == "bookChange" or str == "confirmItem":
                adb.perform_click(1130, 640)
                tools.sleep()
            tools.back()
            tools.back()
            break

    for i in range(3):
        try:
            enterDC()
        except Exception as e:
            raise e
        adb.perform_click(150, 500)
        tools.sleep()
        if tools.match_pics() == "item":
            adb.perform_click(400, 850)
            tools.sleep()
            adb.perform_click(1600, 820)
            tools.sleep()
            adb.perform_click(1500, 970)
            tools.sleep()
            if tools.match_pics() == "bookChange" or str == "confirmItem":
                adb.perform_click(1130, 640)
                tools.sleep()
            tools.back()
            tools.back()
            break


def dormitory():
    try:
        enterDC()
    except Exception as e:
        raise e
    adb.perform_click(750, 800)
    tools.sleep()
    adb.perform_click(350, 1000)
    tools.sleep()


def DispatchCompany():
    getResourse()
    capsuleToy()
    # addBookItem()
    dormitory()
    drinkTea()
    tools.delete_png_files()
    try:
        home.returnHome()
    except Exception as e:
        raise e
