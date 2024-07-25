import adb
import tools
import DispatchCompany
import cv
import Call
import Store
import Fight
import Award
import Mail
import const
import Travel
import os
import json

CONFIG_FILE = "config.json"


def main():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            settings = json.load(f)
            path = settings.get("path", "")
            store = settings.get("store", False)
            mail = settings.get("mail", False)
            DC = settings.get("DC", False)
            call = settings.get("call", False)
            fight = settings.get("fight", False)
            award = settings.get("award", False)
            travel = settings.get("travel", False)
            port = settings.get("port", "")
            strName = ""
            if settings.get("Money", False):
                strName = "Money"
            elif settings.get("Book", False):
                strName = "Book"
            elif settings.get("Weapon", False):
                strName = "Weapon"

    print(f"虚拟机启动！:{path};{port}")
    const.setAdbPath(path, port)
    print("配置完成")
    adb.adb_connect()
    adb.get_wh()
    # print("列出长宽")

    cv.load_feature_data()
    tools.delete_png_files()

    if store:
        Store.store()
    if mail:
        Mail.mail()
    if DC:
        DispatchCompany.DispatchCompany()
    if call:
        Call.call()
    if fight:
        Fight.fight(strName)
    if award:
        Award.award()
    if travel:
        Travel.travel()
    tools.delete_png_files()


if __name__ == "__main__":
    # adb_path = "D:\\leidian\\LDPlayer9\\adb.exe"
    main()
