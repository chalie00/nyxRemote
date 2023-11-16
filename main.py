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
# mainDia.print_control_identifiers(filename='Text\Element_ID.txt')

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
#         # time.sleep(1)
#         mouse.move(coords=(3200, 170))
#         # time.sleep(1)
#         mouse.double_click(coords=(3200, 170))
#     else:
#         print('Nyx is not exist')
#
# # Check whether network config pop-up
# network_popup = app.window(title_re=f'{cons.sys_mac}')
# mf.whether_popup_focus(network_popup, 'OK')
# if mainDia['OK'].exists(timeout=3, retry_interval=1):
#     time.sleep(1)
#     mainDia['OK'].click()

# Execute xml and update in the command tab
# cm.select_cmd_xml_update(mainDia)

# count = 10000
# while count >= 0:
#     mainDia['Clear'].click()
#     ctl.af_after_tele(mainDia, 18000)
#     find_af_log = mf.check_char_in_bottom(mainDia, cons.find_af)
#     if find_af_log == cons.find_af:
#         mainDia.capture_as_image().save(f'Capture\{count - 1}.png')
#         count = count - 1
#     else:
#         print('Tele af is not over')
#
#     mainDia['Clear'].click()
#     ctl.af_after_wide(mainDia, 17000)
#     find_af_log_sec = mf.check_char_in_bottom(mainDia, cons.find_af)
#     if find_af_log_sec == cons.find_af:
#         mainDia.capture_as_image().save(f'Capture\{count - 1}.png')
#         count = count - 1
#     else:
#         print('Wide af is not over')
ctl.loop_zoom_af_capture(mainDia, 1000)