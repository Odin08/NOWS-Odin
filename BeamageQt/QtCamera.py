# -*- coding: utf-8 -*-
#


import matplotlib.pyplot as plt
import numpy as np

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow
from MineGUI import Ui_Dialog
from pyqtgraph.ptime import time

import os

assembly_path = r"BeamagePy\BeamagePy\bin\Debug"
import sys
sys.path.append(assembly_path)

import clr
clr.AddReference("BeamagePy")

from BeamagePyC import BeamageSdk
SDK = BeamageSdk()


# Create colormap
mask = np.arange(0, 2048*2048/4, 2)
bit = np.arange(0, 257, 1)/256
colmap = np.array(255 * plt.cm.nipy_spectral(bit), dtype=np.ubyte)



class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)


def profile(data):
    x = np.sum(data, axis=0)
    y = np.sum(data, axis=1)
    return x/x.max()*100, y/y.max()*100

def grab_image():
    listImage = list(SDK.BeamageGrubImage())
    image = np.array(listImage).reshape(height, width)
    return image

def main():

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


    main.pathBox.setText('X:/gonta/first_test_m2/')
    main.nameBox.setText('name file')
    #n_average = main.spinBox.text()

    timer = QtCore.QTimer()

    def start():
        SDK.BeamageRun()
        timer.start(1)

    def stop():
        SDK.BeamageStop()
        timer.stop()

    def save():
        np.savez_compressed(main.pathBox.text() + main.nameBox.text() + '.npz', a=y)
    '''
    def setText(t_expos, w):
        if t_expos < 1:
            t_expos *= 1000
            t_expos = np.round(t_expos, 0)
        else:
            t_expos = np.round(t_expos, 0)
        w = int(w)
        main.sizeBeam.setText(str(w) + ' mkm')
        main.exposValue.setText(str(t_expos))
    '''

    def update():
        # Obtained data
        cut_n = int(main.spinBox.text())
        data = (grab_image())[::2, ::2]
        # Display image
        img.setImage(data)
        # Display profile
        main.xprof.clear()
        main.yprof.clear()
        main.xprof.plot(profile(data)[0])
        main.yprof.plot(profile(data)[1])

        app.processEvents()

    timer.timeout.connect(update)
    main.startBtn.clicked.connect(start)
    main.stopBtn.clicked.connect(stop)
    main.saveBtn.clicked.connect(save)


    if __name__ == '__main__':
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


app = QtGui.QApplication([])
SDK.BeamageConnect()
width = int(SDK.BeamageGrubSize()[0])
height = int(SDK.BeamageGrubSize()[1])
SDK.SetExposureTime(1.1)
main()
