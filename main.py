import os

from pywinauto import Application, keyboard, mouse

import Constants as cs

# Start the Nyx Remote
app = Application(backend='uia').start(cs.app_path)
mainDia = app['nyxremote_231106']




