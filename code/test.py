import adb
import tools
import DispatchCompany
import cv
import Call
import Store
import Fight
import Award

if __name__ == "__main__":
    device_id = "YOUR_DEVICE_ID"

    # 步骤执行
    adb.connect_device(device_id)
    print("虚拟机启动！")
    adb.package_list()
    # install_app(apk_path)
    print("列出所有package")
    adb.get_wh()
    print("列出长宽")
    # start_app(package_name, activity_name)
    print("手动：物华米线，启动！")

    cv.load_feature_data()

    adb.version()
    tools.press_hold(1000, 500, 10)
