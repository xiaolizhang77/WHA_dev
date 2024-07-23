import tools
import adb
import home


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