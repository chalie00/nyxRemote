import time
import pywinauto

import Constants as cons

from pywinauto import Application


# Check whether Pop-Up is actived and focus the Pop-Up
def whether_popup_focus(popup_window: Application, click_btn: str):
    popup = popup_window
    if popup.exists(timeout=3, retry_interval=1):
        popup.set_focus()
        popup[f'{click_btn}'].click()
    else:
        print('Did not find pop up')


# Calculate center coordinate of specify UI from ltrb(Left Top, Right Bottom)
def cal_center(ui_coord_array_ltrb):
    center_x = ui_coord_array_ltrb[0] + int((ui_coord_array_ltrb[2] - ui_coord_array_ltrb[0]) / 2)
    center_y = ui_coord_array_ltrb[1] + int((ui_coord_array_ltrb[3] - ui_coord_array_ltrb[1]) / 2)

    coord = [center_x, center_y]
    return coord


# Check whether specify character in bottom log
def check_char_in_bottom(dia, char):
    time.sleep(10)
    check_txt = ''
    bottom_txt = (dia
                  .child_window(auto_id='MainWindow.centralwidget.groupBox.editPacketView', control_type='Edit')
                  .window_text())
    convert_txt = open(rf'Text\find_{char}.txt', 'w+')
    for line in bottom_txt:
        convert_txt.write(line)
    convert_txt.close()

    convert_txt = open(rf'Text\find_{char}.txt', 'r')
    convert_txt_arr = convert_txt.readlines()
    for find in convert_txt_arr:
        if char in find:
            print('find the character')
            check_txt = find
        else:
            print('There is not your char')
    print((check_txt[8:43]))
    return check_txt[8:43]
