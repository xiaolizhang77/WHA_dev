import json
import os
import sys
from functools import partial

from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, QObject, QThread
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QCheckBox, QTextEdit

import main


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._running = False
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = EmittingStream(textWritten=self.handle_output)
        sys.stderr = EmittingStream(textWritten=self.handle_output)

    def handle_output(self, text):
        self.progress.emit(text)

    def run(self, path: str, store: bool, mail: bool, DC: bool, call: bool, fight: bool, strName: str, award: bool):
        self._running = True
        main.main(path, store, mail, DC, call, fight, strName, award)

    def stop(self):
        self._running = False


thread = None
worker = Worker()


def run(adb_path: str, store: bool, mail: bool, DC: bool, call: bool, fight: bool, str: str, award: bool):
    global thread, worker
    if thread is None:
        # thread = threading.Thread(target=partial(worker.run, store, mail, DC, call, fight, award))
        # thread.start()
        thread = QThread()
        worker.moveToThread(thread)
        thread.started.connect(partial(worker.run, adb_path, store, mail, DC, call, fight, str, award))
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        thread.start()
    else:
        worker.stop()
        thread.quit()
        thread.wait()
        thread = None


def update_text(textEdit, message):
    textEdit.append(message)


CONFIG_FILE = "config.json"


def load_settings(ui):
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            settings = json.load(f)
            ui.lineEdit.setText(settings.get("path", ""))
            ui.checkBox.setChecked(settings.get("checkBox", False))
            ui.checkBox_2.setChecked(settings.get("checkBox2", False))
            ui.checkBox_3.setChecked(settings.get("checkBox3", False))
            ui.checkBox_4.setChecked(settings.get("checkBox4", False))
            ui.checkBox_5.setChecked(settings.get("checkBox5", False))
            ui.checkBox_6.setChecked(settings.get("checkBox6", False))
            ui.radioButton.setChecked(settings.get("radioButton", False))
            ui.radioButton_2.setChecked(settings.get("radioButton2", False))
            ui.radioButton_3.setChecked(settings.get("radioButton3", False))


def save_settings(ui):
    settings = {
        "path": ui.lineEdit.text(),
        "checkBox": ui.checkBox.isChecked(),
        "checkBox2": ui.checkBox_2.isChecked(),
        "checkBox3": ui.checkBox_3.isChecked(),
        "checkBox4": ui.checkBox_4.isChecked(),
        "checkBox5": ui.checkBox_5.isChecked(),
        "checkBox6": ui.checkBox_6.isChecked(),
        "radioButton": ui.radioButton.isChecked(),
        "radioButton2": ui.radioButton_2.isChecked(),
        "radioButton3": ui.radioButton_3.isChecked(),
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(settings, f)


def getStr(ui):
    strName = ""
    if ui.radioButton.isChecked():
        strName = "Money"
    elif ui.radioButton_2.isChecked():
        strName = "Book"
    elif ui.radioButton_3.isChecked():
        strName = "Weapon"
    return strName


if __name__ == "__main__":
    # adb_path = "D:\\leidian\\LDPlayer9\\adb.exe"
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
    textEdit: QTextEdit = ui.textEdit

    load_settings(ui)
    pushButton.clicked.connect(
        lambda: (
            run(lineEdit.text(), checkBox.isChecked(), checkBox2.isChecked(), checkBox3.isChecked(),
                checkBox4.isChecked(),
                checkBox5.isChecked(), getStr(ui), checkBox6.isChecked()), save_settings(ui)))
    worker.progress.connect(lambda text: update_text(textEdit, text))
    ui.show()
    app.aboutToQuit.connect(lambda: save_settings(ui))
    sys.exit(app.exec())
