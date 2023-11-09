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

# Start the Nyx Remote
app = pywinauto.application.Application(backend='uia')

# Check whether active application
try:
    app.connect(title='NyxRemote_230516')
    # app.kill()
    # time.sleep(1)
    # app = Application(backend='uia').start(cs.app_path)
except (Exception,):
    app = Application(backend='uia').start(cons.app_path)

mainDia = app['nyxremote_231106']
# Save by txt after check an element identify
# mainDia.print_control_identifiers(filename='Text\Element_ID.txt')

mainDia['Clear'].click()
mainDia.Scan.click()


# Device Scan from [Device Scan]
device_scan = app.window(title_re=u'Device Scan...')
if device_scan.exists(timeout=3, retry_interval=1):
    device_scan.set_focus()
    start_btn = device_scan['Start'].click()
    # scan time takes 150sec but for test set a 2 sec
    time.sleep(2)
    # device_scan['Discard'].click()
else:
    print('Did not find Device Scan Pop Up')

# Get the System information
find_nyx_img = im.area_capture_with_coordinate(mainDia,
                                               'right_info',
                                               cons.right_info)
right_info_txt = cf.image_to_string_with_pyocr(cons.right_info_img_path)
memo = open(rf'Text\fight_info.txt', 'w+')
for i in right_info_txt:
    memo.write(i)
memo.close()
memo = open(rf'Text\fight_info.txt', 'r')
txt_arr = memo.readlines()
# Remove a text I from INYX
sys_info = txt_arr[0].split()
# Set the system device info with combine NYX + Device
cons.sys_device = sys_info[0][1:] + ' ' + sys_info[1]
cons.sys_mac = sys_info[3]
cons.sys_ip = sys_info[4]


