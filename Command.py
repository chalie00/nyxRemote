import pywinauto
import time
import threading

import Constants as cons
import Main_Function as mf

from pywinauto import Application
from pynput.keyboard import Key, Controller


# Select command tab and click Update brn after click XML btn
def select_cmd_xml_update(dia):
    dia.child_window(title="Command", control_type="TabItem").click_input()
    dia['XML'].click_input()
    dia['OK'].wait('ready', timeout=10).click()

    dia['Update'].click_input()
    dia['OK'].wait('ready', timeout=20).click()
    dia.child_window(title="Conn", auto_id="MainWindow.centralwidget.btnRtspConn",
                     control_type="Button").click()
    time.sleep(2)
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
