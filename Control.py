import pywinauto
import pyautogui
import time

import terminal

import Constants as cons
import Main_Function as mf

from pynput.keyboard import Key, Controller
from pywinauto import mouse

keyboard = Controller()


# Execute autofocus, after zoom tele or wide to specified encoder value
# 2023.11.22 merge the wide, tele function and near, far can control too
def check_encoder_push_btn_af(dia, encoder: int, increase: bool,
                              child_win: [], btn_coord: [], whether_af: bool):
    flag = True
    dia.child_window(title="Control", control_type="TabItem").click_input()
    distance_coord = mf.get_distance_from_zero(btn_coord)
    print(distance_coord)
    push_btn = mf.cal_center(distance_coord)
    pyautogui.moveTo(push_btn)
    while flag:
        pyautogui.mouseDown(push_btn)
        check_encoder = int((dia.child_window(auto_id=child_win[0], control_type=child_win[1]).window_text()))
        if increase == True and check_encoder >= encoder:
            pyautogui.mouseUp(push_btn)
            print(check_encoder)
            flag = False
        elif increase == False and check_encoder <= encoder:
            pyautogui.mouseUp(push_btn)
            print(check_encoder)
            flag = False
    time.sleep(1)
    if whether_af:
        (dia.child_window(auto_id=cons.af_child[0], control_type=cons.af_child[1]).click())
    elif not whether_af:
        print('AF is not executed')


# Loop which captures after check whether af run and zoom tele/wide/near/far
# 2023.11.22 It was modified to respond to increase or decrease of button
def loop_zoom_af_capture(dia, count, increase: bool, whether_af: bool,  child_win: [],
                         incrs_encdr: int, decrs_encdr: int,
                         incrs_btn_coord: [], decrs_btn_coord: []):
    time_btn_status = dia['Time'].get_toggle_state()
    if time_btn_status:
        print('Time button is checked')
        dia['Time'].click()
    else:
        print('Time button is not checked')
    while count >= 0:
        dia['Clear'].click()
        increase_btn_coord = mf.get_distance_from_zero(incrs_btn_coord)
        check_encoder_push_btn_af(dia, incrs_encdr, increase,
                                  child_win, increase_btn_coord, whether_af)
        find_af_log = mf.check_char_in_bottom(dia, cons.find_af)
        if find_af_log == cons.find_af:
            dia.capture_as_image().save(f'Capture\{count - 1}.png')
            count = count - 1
        else:
            print('Increase af is not over')

        dia['Clear'].click()
        decrease_btn_coord = mf.get_distance_from_zero(decrs_btn_coord)
        check_encoder_push_btn_af(dia, decrs_encdr, not increase,
                                  child_win, decrease_btn_coord, whether_af)
        find_af_log_sec = mf.check_char_in_bottom(dia, cons.find_af)
        if find_af_log_sec == cons.find_af:
            dia.capture_as_image().save(f'Capture\{count - 1}.png')
            count = count - 1
        else:
            print('Decrease af is not over')


# TODO (com 11/22) - OSD menu control
def osd_control(dia, chk_menu: bool, direction: str):
    if chk_menu:
        drct = direction.lower()
        if drct == 'set':
            dia.child_window(title='Set', control_type='Button').click()
        elif drct == 'left':
            dia.child_window(title='Left', control_type='Button').click()
        elif drct == 'right':
            dia.child_window(title='Right', control_type='Button').click()
        elif drct == 'up':
            dia.child_window(title='Up', control_type='Button').click()
        elif drct == 'down':
            dia.child_window(title='Down', control_type='Button').click()
    else:
        print('OSD Menu is not activated')