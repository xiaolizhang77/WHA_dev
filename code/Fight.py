import home
import adb
import tools

emum = {"money","book","weapon"}
def fight(name):
    if name not in emum:
        print("Fight False")
        return
    print("fight start")
    