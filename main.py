# -*- coding: utf-8 -*-
import os
import time

import pyocr
import pywinauto
import pytesseract

from pywinauto import Application, keyboard, mouse
from PIL import Image

import Constants as cons
import Character_Func as cf
import Image_Capture_Func as im
import Main_Function as mf
import Command as cm
import Control as ctl

# Start the Nyx Remote
app = pywinauto.application.Application(backend='uia')

# Check whether active application
try:
    app.connect(title='NyxRemote_230516')
    # app.kill()
    # time.sleep(1)
    # app = Application(backend='uia').start(cos.app_path)
except (Exception,):
    app = Application(backend='uia').start(cons.app_path)

mainDia = app['nyxremote_231106']
# Save by txt after check an element identify
# mf.get_app_zero_pos(mainDia)
# # mainDia.print_control_identifiers(filename='Text\Element_ID.txt')
#
#
# mainDia['Clear'].click()
# time.sleep(1)
# time_btn_status = mainDia['Time'].get_toggle_state()
# if time_btn_status:
#     print('Time button is checked')
#     mainDia['Time'].click()
# else:
#     print('Time button is not checked')
# time.sleep(1)
# mainDia.Scan.click()
#
# device_popup = app.window(title_re=u'Device Scan...')
# # Device Scan from [Device Scan]
# mf.whether_popup_focus(device_popup, 'Start')
#
# # Get the System information
# bottom_txt = (mainDia
#               .child_window(auto_id='MainWindow.centralwidget.groupBox.editPacketView', control_type='Edit')
#               .window_text())
# scan_nyx = open(r'Text\scan_nyx.txt', 'w+')
# for i in bottom_txt:
#     scan_nyx.write(i)
# scan_nyx.close()
#
# # Check whether Nyx is
# # if there is nyx click and get the nyx information from txt
# scan_nyx = open(r'Text\scan_nyx.txt', 'r')
# scan_txt_arr = scan_nyx.readlines()
# for i in scan_txt_arr:
#     if 'NYX.ACK#I_am_NYX' in i:
#         print('I am Nyx')
#         cons.sys_mac = i[25:42]
#         cons.sys_ip = i[43:57]
#         cons.sys_type = i[108:118]
#         cons.sys_len_type = i[119:134]
#         cons.sys_ver = i[135:150]
#         cons.sys_device = i[151:160]
#         cons.sys_rtsp_add = f'rtsp://{cons.sys_ip}:8554/test'
#         mf.whether_popup_focus(device_popup, 'Discard')
#         from_zero_scanned_device = mf.get_distance_from_zero(cons.scanned_only_one_device)
#         time.sleep(1)
#         mouse.move(coords=(from_zero_scanned_device['x'], from_zero_scanned_device['y']))
#         time.sleep(1)
#         mouse.double_click(coords=(from_zero_scanned_device['x'], from_zero_scanned_device['y']))
#     else:
#         print('Nyx is not exist')
#
# # Check whether network config pop-up
# network_popup = app.window(title_re=f'{cons.sys_mac}')
# mf.whether_popup_focus(network_popup, 'OK')
# time.sleep(1)
# if mainDia['OK'].exists(timeout=5, retry_interval=1):
#     time.sleep(1)
#     mainDia['OK'].click()

# # Execute xml and update in the command tab
# cm.select_cmd_xml_update(mainDia)

# ctl.loop_zoom_af_capture(mainDia, 10000, True, True,
#                          cons.focus_enc_child, 8000, -14000,
#                          cons.control_near, cons.control_far)

osd_toggle = mainDia.child_window(title='On/Off', control_type='CheckBox').click_input()
osd_menu_state = mainDia.child_window(title='On/Off', control_type='CheckBox').get_toggle_state()
time.sleep(2)

ctl.osd_control(mainDia, osd_menu_state, 'down')
ctl.osd_control(mainDia, osd_menu_state, 'down')
ctl.osd_control(mainDia, osd_menu_state, 'up')
ctl.osd_control(mainDia, osd_menu_state, 'up')
ctl.osd_control(mainDia, osd_menu_state, 'set')
ctl.osd_control(mainDia, osd_menu_state, 'right')
ctl.osd_control(mainDia, osd_menu_state, 'left')

