# Application Install Path
app_path = r'C:\Users\SC Team\Desktop\00.Local FW\NYX SC-640R\NYXRemote_231106\NyxRemote_231106.exe'

# System info
sys_mac = ''
sys_ip = ''
sys_device = ''
sys_type = ''
sys_ver = ''
sys_len_type = ''
sys_rtsp_add = ''

# Save Directory
right_info_img_path = fr'Capture\right_info_crop.png'
device_info_img_path = fr'Capture\device_info_crop.png'


# Lens Data
focus_lim = [-17000, 10000]  # [Far, Near]
zoom_lim = [16003, 33704]  # [Wide, Tele]
fov_lim = [1.8, 35.1]  # [NFOV, WFOV]

# Main Tab element coordinate
static_zero_Coordinate = [2080, 75, 3680, 975]
float_zero_Coordinate = []

# Coordinate of the device Tab
# right_info = [3149, 158, 3660, 180] only ip
# right_info = [3148, 160, 3625, 180] # 앞에 I 빼고 완벽
# device_info = [3152, 160, 3260, 180] # only Device
device_tab = [3150, 85, 3216, 108]
scanned_only_one_device = [3200, 170, 0, 0]

# Coordinate of the Command Tab
command_tab = [3216, 85, 3289, 108]

# Coordinate of the Control Tab
control_tab = [3289, 85, 3362, 108]
control_af = [3240, 158, 3320, 180]
control_narrow = [3240, 131, 3320, 153]
control_wide = [3240, 185, 3320, 207]
control_far = [3157, 158, 3237, 180]
control_near = [3322, 158, 3402, 180]

# Child window of the Control Tab
af_child = ['MainWindow.centralwidget.tabPannel.qt_tabwidget_stackedwidget.tabControl.groupLens.btnLensAF', 'Button']
zoom_enc_child = ['MainWindow.centralwidget.tabPannel.qt_tabwidget_stackedwidget.tabControl.groupLens.labelZoomEnc', 'Text']
focus_enc_child = ['MainWindow.centralwidget.tabPannel.qt_tabwidget_stackedwidget.tabControl.groupLens.labelFocusEnc', 'Text']
fov_enc_child = ['MainWindow.centralwidget.tabPannel.qt_tabwidget_stackedwidget.tabControl.groupLens.labelFOV', 'Text']
menu_chk_box = ['MainWindow.centralwidget.tabPannel.qt_tabwidget_stackedwidget.tabControl.groupMenu.checkMenuOn', 'CheckBox']


# Coordinate of the Special
special_tab = [3362, 85, 3435, 108]

# Coordinate of the information
information_tab = [3435, 85, 3536, 108]

# Coordinate of the factory
factory_tab = [3536, 85, 3609, 108]

# bottom log tab
bottom_log = [2095, 740, 3579, 948]

find_af = 'NYX.ACK#syst_stat=standby&lens_fpos'
