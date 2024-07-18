import home
import adb
import tools


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
