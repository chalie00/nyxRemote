import pywinauto
import pyautogui
import time

import terminal

import Constants as cons
import Main_Function as mf

from pynput.keyboard import Key, Controller
from pywinauto import mouse

keyboard = Controller()


# Execute autofocus, after zoom tele to specified encoder value
def af_after_tele(dia, encoder):
    flag = True
    dia.child_window(title="Control", control_type="TabItem").click_input()
    move_narrow = mf.cal_center(cons.control_narrow)
    pyautogui.moveTo(move_narrow)
    while flag:
        pyautogui.mouseDown(move_narrow)
        check_encoder = int((dia.child_window
                             (auto_id="MainWindow.centralwidget.tabPannel."
                                      "qt_tabwidget_stackedwidget"
                                      ".tabControl.groupLens.labelZoomEnc",
                              control_type="Text")
                             .window_text()))
        if check_encoder >= encoder:
            pyautogui.mouseUp(move_narrow)
            print(check_encoder)
            flag = False
    time.sleep(1)
    (dia.child_window
     (auto_id="MainWindow.centralwidget.tabPannel"
              ".qt_tabwidget_stackedwidget"
              ".tabControl.groupLens.btnLensAF",
      control_type="Button")
     .click())


# Execute autofocus, after zoom wide to specified encoder value
def af_after_wide(dia, encoder):
    flag = True
    move_wide = mf.cal_center(cons.control_wide)
    pyautogui.moveTo(move_wide)
    while flag:
        pyautogui.mouseDown(move_wide)
        check_encoder = int((dia.child_window
                             (auto_id="MainWindow.centralwidget.tabPannel"
                                      ".qt_tabwidget_stackedwidget"
                                      ".tabControl.groupLens.labelZoomEnc",
                              control_type="Text")
                             .window_text()))
        if check_encoder <= encoder:
            pyautogui.mouseUp(move_wide)
            print(check_encoder)
            flag = False
    time.sleep(1)
    (dia.child_window
     (auto_id="MainWindow.centralwidget.tabPannel"
              ".qt_tabwidget_stackedwidget"
              ".tabControl.groupLens.btnLensAF",
      control_type="Button")
     .click())


# Loop which captures after check whether af run and zoom tele/wide
def loop_zoom_af_capture(dia, count):
    while count >= 0:
        dia['Clear'].click()
        af_after_tele(dia, 18000)
        find_af_log = mf.check_char_in_bottom(dia, cons.find_af)
        if find_af_log == cons.find_af:
            dia.capture_as_image().save(f'Capture\{count - 1}.png')
            count = count - 1
        else:
            print('Tele af is not over')

        dia['Clear'].click()
        af_after_wide(dia, 17000)
        find_af_log_sec = mf.check_char_in_bottom(dia, cons.find_af)
        if find_af_log_sec == cons.find_af:
            dia.capture_as_image().save(f'Capture\{count - 1}.png')
            count = count - 1
        else:
            print('Wide af is not over')