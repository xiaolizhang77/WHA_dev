# -*- coding: utf-8 -*-
import json
import os
import sys
from functools import partial
from PyQt6.QtGui import QIcon
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, QObject, QThread
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QCheckBox, QTextEdit

import main

CONFIG_FILE = "config.json"
LOG_FILE = "log.txt"


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

    def run(self):
        self._running = True
        main.main()

    def stop(self):
        self._running = False


thread = None
worker = Worker()


def run():
    global thread, worker
    if thread is None:
        # thread = threading.Thread(target=partial(worker.run, store, mail, DC, call, fight, award))
        # thread.start()
        thread = QThread()
        worker.moveToThread(thread)
        thread.started.connect(partial(worker.run))
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
    with open(LOG_FILE, 'a') as file:
        file.write(message)


def load_settings(ui):
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            settings = json.load(f)
            ui.lineEdit.setText(settings.get("path", ""))
            ui.checkBox.setChecked(settings.get("store", False))
            ui.checkBox_2.setChecked(settings.get("mail", False))
            ui.checkBox_3.setChecked(settings.get("DC", False))
            ui.checkBox_4.setChecked(settings.get("call", False))
            ui.checkBox_5.setChecked(settings.get("fight", False))
            ui.checkBox_6.setChecked(settings.get("award", False))
            ui.checkBox_7.setChecked(settings.get("travel", False))
            ui.checkBox_8.setChecked(settings.get("tea", False))
            ui.radioButton.setChecked(settings.get("Money", False))
            ui.radioButton_2.setChecked(settings.get("Book", False))
            ui.radioButton_3.setChecked(settings.get("Weapon", False))
            ui.lineEdit_2.setText(settings.get("port", ""))


def save_settings(ui):
    settings = {
        "path": ui.lineEdit.text(),
        "store": ui.checkBox.isChecked(),
        "mail": ui.checkBox_2.isChecked(),
        "DC": ui.checkBox_3.isChecked(),
        "call": ui.checkBox_4.isChecked(),
        "fight": ui.checkBox_5.isChecked(),
        "award": ui.checkBox_6.isChecked(),
        "travel": ui.checkBox_7.isChecked(),
        "tea": ui.checkBox_8.isChecked(),
        "Money": ui.radioButton.isChecked(),
        "Book": ui.radioButton_2.isChecked(),
        "Weapon": ui.radioButton_3.isChecked(),
        "port": ui.lineEdit_2.text()
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(settings, f)


# def getStr(ui):
#     strName = ""
#     if ui.radioButton.isChecked():
#         strName = "Money"
#     elif ui.radioButton_2.isChecked():
#         strName = "Book"
#     elif ui.radioButton_3.isChecked():
#         strName = "Weapon"
#     return strName


if __name__ == "__main__":

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    # adb_path = "D:\\leidian\\LDPlayer9\\adb.exe"
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.ico'))  # 设置任务栏图标
    ui = uic.loadUi("./ui/WHA.ui")
    lineEdit: QLineEdit = ui.lineEdit
    checkBox: QCheckBox = ui.checkBox
    checkBox2: QCheckBox = ui.checkBox_2
    checkBox3: QCheckBox = ui.checkBox_3
    checkBox4: QCheckBox = ui.checkBox_4
    checkBox5: QCheckBox = ui.checkBox_5
    checkBox6: QCheckBox = ui.checkBox_6
    checkBox7: QCheckBox = ui.checkBox_7
    checkBox8: QCheckBox = ui.checkBox_8
    pushButton: QPushButton = ui.pushButton
    textEdit: QTextEdit = ui.textEdit
    lineEdit2: QLineEdit = ui.lineEdit_2

    load_settings(ui)
    pushButton.clicked.connect(lambda: (run(), save_settings(ui)))
    worker.progress.connect(lambda text: update_text(textEdit, text))
    ui.show()
    app.aboutToQuit.connect(lambda: save_settings(ui))
    sys.exit(app.exec())
