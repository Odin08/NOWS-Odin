# -*- coding: utf-8 -*-
#
import sys

import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.ptime import time
from MineGUI import Ui_Dialog

import time as tm
import os

from instrumental.drivers.cameras import uc480
import translator as tl



# Create colormap
mask = np.arange(0, 2048*2048, 2)
bit = np.arange(0, 257, 1)/256
colmap = np.array(255 * plt.cm.nipy_spectral(bit), dtype=np.ubyte)




class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)


def profile(data):
    x = np.sum(data, axis=0)
    y = np.sum(data, axis=1)
    x = x - np.mean(x[:10])
    y = y - np.mean(y[:10])
    return x/x.max()*100, y/y.max()*100


def grab_image(T):
    framerate = 1. / Q_(T, "second")
    cap._dev.SetFrameRate(framerate.m_as('Hz'))
    frame = cap.grab_image(timeout="1.5 s", exposure_time=Q_(T, "second"), fix_hotpixels=True)
    frame.astype(float)
    return frame

def change_exposure(arr, t):
    tmin, tmax, q = 20e-3, 0.3, 7 / 8.
    if (arr.max() > 800):
        t = t * q
        if (t < tmin): t = tmin
    elif (arr.max() < 700) and (t is not tmax):
        t = t / q
        if (t > tmax): t = tmax
    return t

def main():
    global Tau
    # Settings of camera ----------------------------------------------------------------------------------------
    cap = uc480.UC480_Camera()  # init the camera
    Tau = 0.04  # second
    framerate = 1. / Q_(Tau, "second")
    cap._dev.SetFrameRate(framerate.m_as('Hz'))
    cap.auto_blacklevel = False
    # cap.blacklevel_offset = 230
    Zero_array = np.array(cap.grab_image(timeout="0.3 s", exposure_time=Q_(0.001, "second"), fix_hotpixels=True))
    Zero_array.astype(float)
    np.savez_compressed('X:/gonta/CloudData-2019/ThorCam/black_level/1.npz', a=Zero_array)
    Zero_array[:, :] = 0  # array for average of images
    average_frame = np.copy(Zero_array)
    # ------------------------------------------------------------------------------------------------------------

    main = MainWindow()
    main.show()
    # Add ViewBox for Image
    view = pg.ViewBox()
    main.imshow.setCentralItem(view) # (main.imshow = pg.GraphicsView(Dialog) from MineGUI)
    # Add Image Item and set colormap
    img = pg.ImageItem()
    cmap = pg.ColorMap(bit, colmap)
    lut = cmap.getLookupTable(0.0, 1.0, 255)
    img.setLookupTable(lut)
    img.setAutoDownsample(True)
    img.setBorder('b')

    view.addItem(img)


    main.pathBox.setText('X:/gonta/CloudData-2019/ThorCam/')
    main.nameBox.setText('name file')
    #n_average = main.spinBox.text()

    timer = QtCore.QTimer()


    def start():
        timer.start(1)

    def stop():
        timer.stop()

    def save():
        global data
        np.savez_compressed(main.pathBox.text() + main.nameBox.text() + '.npz', a=y)
        #read -- loaded = np.load(main.pathBox.text() + main.nameBox.text() + '.npz')['a']

    def setText(t_expos, w):
        if t_expos < 1:
            t_expos *= 1000
            t_expos = np.round(t_expos, 0)
        else:
            t_expos = np.round(t_expos, 0)
        w = int(w)
        main.sizeBeam.setText(str(w) + ' mkm')
        main.exposValue.setText(str(t_expos))

    def m2():
        global m2_flag, device_id, m2_flag_home, flag_i
        pos = int((tl.test_get_position(device_id)[0])*2.56e-3)
        if pos < 100:
            tl.follow_home(device_id)
            m2_flag_home = True
        if pos > 100:
            tl.test_move(device_id, tl.pos(200), 0)
            tl.test_wait_for_stop(device_id, 100)
        m2_flag = True
        flag_i = 0

    global lastTime, numStep, image, m2_flag
    lastTime = time()
    numStep = 0
    m2_flag = False

    l = np.arange([0, 20, 30, 40, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 160, 180, 200])


    def update():
        global image, Tau, m2_flag, device_id, m2_flag_home, flag_i

        image =  grab_image(Tau)
        Tau = change_exposure(image, Tau)

        img.setImage(image)

        main.xprof.clear()
        main.yprof.clear()
        main.xprof.plot(profile(image)[0])
        main.yprof.plot(profile(image)[1])

        if m2_flag == True:
            if (Tau < 20e-3) and (Tau > 0.3):
                if m2_flag_home == True:
                    np.savez_compressed(main.pathBox.text() + str(l[flag_i]), a=image)
                    tl.test_move(device_id, int(tl.pos(l[flag_i])), 0)
                    tl.test_wait_for_stop(device_id, 100)
                    flag_i += 1
                    if flag_i == (len(l) - 1):
                        m2_flag = False
                else:
                    lr = l[::-1]
                    np.savez_compressed(main.pathBox.text() + str(lr[flag_i]), a=image)
                    tl.test_move(device_id, int(tl.pos(lr[flag_i])), 0)
                    tl.test_wait_for_stop(device_id, 100)
                    flag_i += 1
                    if flag_i == (len(l) - 1):
                        m2_flag = False


        setText(t_expos, (dx + dy)/4.)
        app.processEvents()


    timer.timeout.connect(update)
    main.startBtn.clicked.connect(start)
    main.stopBtn.clicked.connect(stop)
    main.saveBtn.clicked.connect(save)

    main.M2Btn.clicked.connect(m2)

    if __name__ == '__main__':
        import sys

        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


device_id = tl.main()
tl.test_set_speed(device_id, 1024)

pixel = 5.3e-3
app = QtGui.QApplication([])

main()

