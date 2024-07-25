# adb.exe的路径
adb_path = ""
adb_port = ""

directory = "./pic"

# 已知界面的截图路径
known_screenshot_paths = {
    "bilibili": "./known_pic/bilibili.png",
    "ld_home": "./known_pic/ld_home.png",

    "calendar": "./known_pic/calendar.png",

    "getThings": "./known_pic/getThings.png",

    "home": "./known_pic/home.png",
    "office": "./known_pic/office.png",
    "book": "./known_pic/book.png",
    "bookChange": "./known_pic/bookChange.png",
    "dispatchCompany": "./known_pic/dispatchCompany1.png",
    "item": "./known_pic/item.png",
    "machine": "./known_pic/machine.png",
    "dormitory": "./known_pic/dormitory.png",
    "confirmItem": "./known_pic/confirmItem.png",

    "callMain": "./known_pic/callMain.png",
    "callNum": "./known_pic/callNum.png",
    "callEnd": "./known_pic/callEnd.png",
    "confirmCall0": "./known_pic/confirmCall_0.png",
    "confirmCall1": "./known_pic/confirmCall_1.png",
    "confirmCall2": "./known_pic/confirmCall_2.png",
    "confirmCall3": "./known_pic/confirmCall_3.png",
    "confirmCall4": "./known_pic/confirmCall_4.png",
    "confirmCall5": "./known_pic/confirmCall_5.png",
    "confirmCall6": "./known_pic/confirmCall_6.png",
    "confirmCall7": "./known_pic/confirmCall_7.png",
    "callEnd2": "./known_pic/callEnd2.png",

    "store": "./known_pic/store.png",
    "package": "./known_pic/package.png",

    "dailyAward": "./known_pic/dailyAward.png",
    "weeklyAward": "./known_pic/weeklyAward.png",

    "fight": "./known_pic/fight.png",
    "fightMoney": "./known_pic/fightMoney.png",
    "fightMoneyFive": "./known_pic/fightMoneyFive.png",
    "fightMoneyNum": "./known_pic/fightMoneyNum.png",
    "fightEnd": "./known_pic/fightEnd.png",
    "fighting": "./known_pic/fighting.png",
    "fightBook": "./known_pic/fightBook.png",
    "fightBookFive": "./known_pic/fightBookFive.png",
    "fightBookNum": "./known_pic/fightBookNum.png",
    "fightWeapon": "./known_pic/fightWeapon.png",
    "fightWeaponFive": "./known_pic/fightWeaponFive.png",
    "fightWeaponNum": "./known_pic/fightWeaponNum.png",

    "heartFull": "./known_pic/heartFull.png",

    "mail": "./known_pic/mail.png",

    "travel": "./known_pic/travel.png",

    "teaHouse": "./known_pic/teaHouse.png",
    "teaGet": "./known_pic/teaGet.png",
    "teaChoice": "./known_pic/teaChoice.png",
    "teaInvite": "./known_pic/teaInvite.png",
    "teaTalk": "./known_pic/TeaTalk.png",
    "teaWait": "./known_pic/teaWait.png",
}

#   已知界面的特征区域
known_screenshot_area = {
    "home": [1360, 575, 250, 200],
    "office": [0, 0, 400, 100],
    "store": [0, 0, 400, 100],
    "package": [500, 250, 500, 500],
    "dailyAward": [0, 0, 400, 100],
    "weeklyAward": [0, 0, 400, 100],
    "callEnd2": [800, 900, 300, 70],
    "fight": [0, 0, 400, 100],
    "fightMoneyFive": [0, 0, 400, 250],
    "fightMoneyNum": [800, 600, 650, 240],
    "fighting": [1020, 0, 900, 250],
    "fightEnd": [1020, 0, 900, 250],
    "heartFull": [600, 350, 700, 380],
    "confirmItem": [600, 350, 700, 380],
    "bookChange": [600, 350, 700, 380],
    "mail": [0, 0, 400, 100],
    "fightWeaponFive": [0, 0, 400, 250],
    "fightWeaponNum": [800, 600, 650, 240],
    "fightBookFive": [0, 0, 400, 250],
    "fightBookNum": [800, 600, 650, 240],
    "travel": [0, 0, 400, 100],

    "teaHouse": [0, 0, 400, 100],
    "teaTalk": [0, 0, 400, 100],
    "teaGet": [1080, 220, 160, 160],
}

button = {
    "travel": ["travel", [1050, 960, 230, 80]],

    "teaChoice": ["teaHouse", [0, 600, 200, 400]],
    "teaInvite": ["teaHouse", [1680, 900, 170, 120]],
    "teaWait": ["teaHouse", [40, 870, 150, 150]],
}


def setAdbPath(path: str, port: str):
    global adb_path, adb_port
    adb_path = path
    adb_port = port
