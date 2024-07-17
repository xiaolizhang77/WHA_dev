import home
import adb
import tools

def store():
    print("Buy Package")
    try:
        home.returnHome()
    except Exception as e:
        raise e
    adb.perform_click(1370, 1000)
    tools.sleep()
    # todo
    adb.perform_click(1000, 200)
    tools.sleep()
    if  tools.match_pics() == "store":
        adb.perform_click(250, 600)
        tools.sleep()
        adb.perform_click(550, 980)
        tools.sleep()
    else:
        raise Exception("Buy Package Error")
    if tools.match_pics() == "package":
        adb.perform_click(1220,800)
        tools.sleep()
    tools.back()

    tools.delete_png_files()