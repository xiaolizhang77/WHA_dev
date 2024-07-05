import home
import adb
import tools


def enterDC():
    for i in range(5):
        if tools.match_pics() == "dispatchCompany":
            print("进入派遣公司")
            return
        print("????")
        try:
            home.returnHome()
        except Exception as e:
            raise e
        adb.perform_click(1750, 740)
        tools.sleep()
    raise Exception("Error")


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
    raise Exception("Error")


def drinkTea():
    print("Drinking Tea")


def capsuleToy():
    for i in range(5):
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
            return
        elif tools.match_pics() == "office":
            print("扭过了")
            return
    print("扭蛋机完成")
    adb.perform_click(70, 50)
    tools.sleep()


def addBookItem():
    print("Adding Book Item")


def DispatchCompany():
    getResourse()
    capsuleToy()
    addBookItem()
    drinkTea()
