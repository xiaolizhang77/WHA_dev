from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QCheckBox
from PyQt6 import uic
import sys
import main
import 

def run(store: bool, mail: bool, DC: bool, call: bool, fight: bool, award: bool):
    main.main(store, mail, DC, call, fight, "Money", award)

def test():
    print("ok")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = uic.loadUi("./ui/WHA.ui")
    lineEdit: QLineEdit = ui.lineEdit
    checkBox: QCheckBox = ui.checkBox
    checkBox2: QCheckBox = ui.checkBox_2
    checkBox3: QCheckBox = ui.checkBox_3
    checkBox4: QCheckBox = ui.checkBox_4
    checkBox5: QCheckBox = ui.checkBox_5
    checkBox6: QCheckBox = ui.checkBox_6
    pushButton: QPushButton = ui.pushButton


    pushButton.clicked.connect(
        lambda: run(checkBox.isChecked(), checkBox2.isChecked(), checkBox3.isChecked(), checkBox4.isChecked(),
                    checkBox5.isChecked(), checkBox6.isChecked()))

    ui.show()

    sys.exit(app.exec())
