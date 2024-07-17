import adb
import tools
import DispatchCompany
import cv
import Call
import Store
import Fight
import Award
import Mail


def main(store: bool, mail: bool, DC: bool, call: bool, fight: bool, str: str, award: bool):
    # device_id = "YOUR_DEVICE_ID"
    # adb.connect_device(device_id)
    print("虚拟机启动！")
    # adb.package_list()
    # print("列出所有package")
    adb.get_wh()
    print("列出长宽")

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
        Fight.fight(str)
    if award:
        Award.award()
    tools.delete_png_files()


if __name__ == "__main__":
    main(True, True, True, True, True, "Money", True)
