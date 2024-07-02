import subprocess
import const
def run_adb_command(command):
    full_command = f"{const.adb_path} {command}"
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

# 1. 连接设备
def connect_device(device_id):
    run_adb_command(f"connect {device_id}")

# 2. 安装应用
def install_app(apk_path):
    run_adb_command(f"install {apk_path}")

# 3. 启动应用
def start_app(package_name, activity_name):
    run_adb_command(f"shell am start -n {package_name}/{activity_name}")

# 4. 执行一些操作
def perform_click(x, y):
    run_adb_command(f"shell input tap {x} {y}")

def input_text(text):
    run_adb_command(f"shell input text '{text}'")

# 5. 获取日志
def get_logcat():
    run_adb_command("logcat -d")

# 6. 卸载应用
def uninstall_app(package_name):
    run_adb_command(f"uninstall {package_name}")

def package_list():
    run_adb_command("shell pm list packages")

def get_wh():
    run_adb_command("shell wm size")

def get_screen_cut(screenshot_name):
    run_adb_command(f"shell screencap /sdcard/{screenshot_name}")
    run_adb_command(f"pull /sdcard/{screenshot_name} ./pic")
    run_adb_command(f"shell rm /sdcard/{screenshot_name}")
