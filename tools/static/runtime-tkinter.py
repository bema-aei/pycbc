import os, sys
dir = os.path.join(sys._MEIPASS, 'tcl')
if not os.path.exists(dir):
    os.makedirs(dir)
dir = os.path.join(sys._MEIPASS, 'tk')
if not os.path.exists(dir):
    os.makedirs(dir)
