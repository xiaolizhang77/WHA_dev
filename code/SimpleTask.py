import home
import adb
import tools


def store():
    print("领取礼包")
    try:
        home.returnHome()
    except Exception as e:
        raise e
    adb.perform_click(1370, 1000)
    tools.sleep()
    # todo
    adb.perform_click(1000, 200)
    tools.sleep()
    if tools.match_pics() == "store":
        adb.perform_click(250, 600)
        tools.sleep()
        adb.perform_click(550, 980)
        tools.sleep()
    else:
        raise Exception("领取礼包失败")
    if tools.match_pics() == "package":
        adb.perform_click(1220, 800)
        tools.sleep()
    tools.back()

    tools.delete_png_files()

def travel():
    for i in range(3):
        try:
            home.returnHome()
        except Exception as e:
            print(e)
            continue
        adb.perform_click(1200, 1000)
        tools.sleep()

        if tools.match_pics() != "travel":
            print("Travel Error")
            continue

        adb.perform_click(100, 450)
        tools.sleep()

        adb.perform_click(340, 330)
        tools.sleep()

        while tools.match_buttons("travel"):
            adb.perform_click(1150, 1000)
            tools.sleep()
            adb.perform_click(500, 1000)
            tools.sleep()

        if tools.match_pics() != "travel":
            print("Travel Error")
            continue

        adb.perform_click(100, 450)
        tools.sleep()

        adb.perform_click(610, 330)
        tools.sleep()

        while tools.match_buttons("travel"):
            adb.perform_click(1150, 1000)
            tools.sleep()
            adb.perform_click(500, 1000)
            tools.sleep()

        if tools.match_pics() != "travel":
            print("Travel Error")
            continue

        adb.perform_click(100, 250)
        tools.sleep()

        while tools.match_buttons("travel"):
            adb.perform_click(1150, 1000)
            tools.sleep()
            adb.perform_click(500, 1000)
            tools.sleep()

        break


def award():
    print("Award")
    try:
        home.returnHome()
    except Exception as e:
        raise e
    adb.perform_click(1770, 1000)
    tools.sleep()
    if tools.match_pics() == "dailyAward":
        adb.perform_click(1200, 1000)
        tools.sleep()
        adb.perform_click(1200, 1000)
        tools.sleep()
        adb.perform_click(1200, 1000)
        tools.sleep()
    else:
        print("Award Error")

    adb.perform_click(200, 500)
    tools.sleep()
    if tools.match_pics() == "weeklyAward":
        adb.perform_click(1200, 1000)
        tools.sleep()
        adb.perform_click(1200, 1000)
        tools.sleep()
        adb.perform_click(1200, 1000)
        tools.sleep()
    else:
        print("Award Error")

    tools.back()

    tools.delete_png_files()


def mail():
    try:
        home.returnHome()
    except Exception as e:
        print(e)
        return
    adb.perform_click(60, 820)
    tools.sleep()
    if tools.match_pics() == "mail":
        adb.perform_click(180, 1000)
        tools.sleep()
    else:
        print("获取邮件失败")
        return
    try:
        home.returnHome()
    except Exception as e:
        print(e)
        return

    tools.delete_png_files()