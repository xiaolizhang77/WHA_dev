import home
import adb
import tools

emum = {"Money", "Book", "Weapon"}


def fight(name):
    if name not in emum:
        print("Fight False")
        return
    print("fight start")
    for i in range(5):
        try:
            home.returnHome()
        except Exception as e:
            print(e)
            return
        adb.perform_click(1500, 450)
        tools.sleep()
        if tools.match_pics() != "fight":
            continue
        adb.perform_click(730, 870)
        tools.sleep()

        if name == "Money":
            adb.perform_click(200, 250)
            tools.sleep()
        elif name == "Book":
            adb.perform_click(200, 380)
            tools.sleep()
        elif name == "Weapon":
            adb.perform_click(200, 500)
            tools.sleep()

        if tools.match_pics() == f"fight{name}":
            adb.perform_click(1650, 535)
            tools.sleep()
        else:
            continue
        break

    if tools.match_pics() != f"fight{name}Five":
        print("Fight Error")
        return

    adb.perform_click(1540, 980)
    tools.sleep()

    if tools.match_pics() != f"fight{name}Num":
        print("Fight Error")
        return

    tools.press_hold(1350, 500, 3)
    tools.sleep()

    if tools.match_pics() != f"fight{name}Num":
        print("Fight Error")
        return

    adb.perform_click(1280, 620)
    tools.sleep()

    if tools.match_pics() == "heartFull":
        adb.perform_click(1150, 630)
        tools.sleep()

    for i in range(100):
        tools.sleep()
        str = tools.match_pics()
        if str == "fightEnd":
            break
        elif str == "fighting":
            continue
        else:
            print("Fight Error")
            return

    if tools.match_pics() != f"fightEnd":
        print("Fight Error")
        return

    tools.sleep()
    adb.perform_click(1660, 950)
    tools.sleep()

    tools.delete_png_files()
