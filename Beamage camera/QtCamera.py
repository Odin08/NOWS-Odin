# -*- coding: utf-8 -*-
#
import sys

import matplotlib.pyplot as plt
import numpy as np

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow
from MineGUI import Ui_Dialog
from pyqtgraph.ptime import time
import time as tm

import datetime
import struct
import os


import translator as tl
import time as tm


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


def sendCommand(handle, cmd): #Создаем функцию для посылания команд
    cmd = ''.join([c+'\0' for c in cmd])
    cmd_bytearr = bytearray(cmd, 'utf8')
    win32file.WriteFile(fileHandle, cmd_bytearr, None)
    win32file.FlushFileBuffers(fileHandle)
    left, data = win32file.ReadFile(fileHandle, 4096)
    return data[:-2:2]

def grab_image():
    data_file = directory + '/' + os.listdir(directory)[0]
    with open(data_file, 'rb') as f:
        f.read(8)
        s = f.read(8)
        area = np.fromstring(s, dtype=np.int32)
        f.read(20)
        sx = f.read(4)
        sy = f.read(4)
        dx = struct.unpack('f', sx)[0]
        dy = struct.unpack('f', sy)[0]
        f.read(41)
        expos = f.read(4)
        t_expos = struct.unpack('f', expos)[0]
        f.read(357)
        img = np.fromstring(f.read(area[0] * area[1] * 4), dtype=np.int).reshape(area[0], area[1])
    os.remove(data_file)
    img[img < 0] = 0
    img = img[10:,:]
    return img, dx, dy, t_expos

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
        sendCommand(fileHandle, '*CTLSTART')
        #sendCommand(fileHandle, '*CTLIMGSAVE')  # Записываем изображение в формате BMG
        timer.start(1)

    def stop():
        sendCommand(fileHandle, '*CTLSTOP')
        shutil.rmtree('Z:/Documents/Gentec-EO', ignore_errors=True)
        timer.stop()


    def save():
        global data
        np.savez_compressed(main.pathBox.text() + main.nameBox.text() + '.npz', a=y)
        #read -- loaded = np.load(main.pathBox.text() + main.nameBox.text() + '.npz')['a']
        #df.to_csv(main.pathBox.text() + main.nameBox.text() + '.csv.gz', index=False, header=False, compression='gzip')

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
        global m2_flag
        m2_flag = True

    global lastTime, numStep, image, m2_flag
    lastTime = time()
    numStep = 0
    m2_flag = False



    def update():
        global lastTime, numStep, image, m2_flag, device_id
        # Obtained data
        cut_n = int(main.spinBox.text())
        sendCommand(fileHandle, '*CTLIMGSAVE')  # Записываем изображение в формате BMG
        image, dx, dy, t_expos =  grab_image()
        #data = (grab_image())[::int(cut_n), ::int(cut_n)]
        # Display image
        img.setImage(image[::cut_n, ::cut_n])
        # Display profile
        main.xprof.clear()
        main.yprof.clear()
        main.xprof.plot(profile(image)[0])
        main.yprof.plot(profile(image)[1])

        if m2_flag == True:
            if (t_expos < 0.150) and (t_expos > 0.005):
                if numStep == 0:
                    device_id = tl.main()
                    tl.test_set_speed(device_id, 1024)
                    tl.follow_home(device_id)
                    tm.sleep(2)
                # sendCommand(fileHandle, '*CTLSTOP')
                pos, upos = tl.test_get_position(device_id)
                pos = round(pos * 2.56e-3, 1)
                np.savez_compressed(main.pathBox.text() + str(pos), a=image)

                if numStep < 10:
                    tl.test_move(device_id, int(tl.pos((numStep + 1) * 2)), 0)
                    tl.test_wait_for_stop(device_id, 100)
                else :
                    m2_flag = False
                    numStep = -1
                numStep += 1




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


fileHandle = win32file.CreateFile("\\\\.\\pipe\\pipe_beamage", win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                                  0, None, win32file.OPEN_EXISTING, 0, None)  # Файл работы с камерой

date = datetime.datetime.now()
if date.month < 10:
    if date.day < 10:
        directory = 'Z:/Documents/Gentec-EO/' + str(date.year) + '/0' + str(date.month) + '/0' + str(date.day)
    else:
        directory = 'Z:/Documents/Gentec-EO/' + str(date.year) + '/0' + str(date.month) + '/' + str(date.day)
else:
    if date.day < 10:
        directory = 'Z:/Documents/Gentec-EO/' + str(date.year) + '/' + str(date.month) + '/0' + str(date.day)
    else:
        directory = 'Z:/Documents/Gentec-EO/' + str(date.year) + '/' + str(date.month) + '/' + str(date.day)

import shutil
shutil.rmtree('Z:/Documents/Gentec-EO', ignore_errors=True)

app = QtGui.QApplication([])

main()
win32file.CloseHandle(fileHandle)
