import re
import time
import pywinauto

import Constants as cons

from pywinauto import Application


# TODO (com 11/16) - Get the Application start zero position
def get_app_zero_pos(dia):
    print('Get the float zero position')
    dia.child_window(title="Device", control_type="TabItem").click_input()
    zero_pos_txt: str
    dia.print_control_identifiers(filename='Text\get_zero_pos.txt')
    ele_txt = open(rf'Text\get_zero_pos.txt', 'r')
    ele_txt_arr = ele_txt.readlines()
    for line in ele_txt_arr:
        if 'Dialog - ' in line:
            zero_pos_txt = line
    zero_pos_int = list(map(int, re.findall('\d+', zero_pos_txt)))
    if len(zero_pos_int) > 4:
        zero_pos_int.remove(zero_pos_int[0])
    cons.float_zero_Coordinate = zero_pos_int
    print(cons.float_zero_Coordinate)


# TODO (com 11/22) - convert element coordinate by based app zero coordinate
# Distance from application zero position to each element
def get_distance_from_zero(element_coord):
    distance = [element_coord[0] - cons.static_zero_Coordinate[0] + cons.float_zero_Coordinate[0],
                element_coord[1] - cons.static_zero_Coordinate[1] + cons.float_zero_Coordinate[1],
                element_coord[2],
                element_coord[3]
                ]

    return distance


# Check whether Pop-Up is activated and focus the Pop-Up
def whether_popup_focus(popup_window: Application, click_btn: str):
    popup = popup_window
    if popup.exists(timeout=5, retry_interval=1):
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


# Check whether specify character in the bottom log
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

