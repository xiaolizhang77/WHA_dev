import home
import adb
import tools

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
    else:
        print("")

    adb.perform_click(200, 500)
    tools.sleep()
    if tools.match_pics() == "weeklyAward":
        adb.perform_click(1200, 1000)
        tools.sleep()
        adb.perform_click(1200, 1000)
        tools.sleep()
    else:
        raise Exception()

    tools.back()
