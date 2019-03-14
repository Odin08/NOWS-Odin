# -*- coding: utf-8 -*-

import sys

import matplotlib.pyplot as plt
import numpy as np
import time as tm
import win32file
import datetime
import struct
import os

from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.ptime import time
import pyqtgraph as pg

from PyQt5.QtWidgets import QMainWindow

from MineGUI_noviz import Ui_Dialog
import translator as tl



class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)

def sendCommand(handle, cmd): #Создаем функцию для посылания команд
    cmd = ''.join([c+'\0' for c in cmd])
    cmd_bytearr = bytearray(cmd, 'utf8')
    win32file.WriteFile(fileHandle, cmd_bytearr, None)
    win32file.FlushFileBuffers(fileHandle)
    left, data = win32file.ReadFile(fileHandle, 4096)
    return data[:-2:2]

def grab_image():
    tm.sleep(3)
    sendCommand(fileHandle, '*CTLSTOP')
    tm.sleep(2)
    sendCommand(fileHandle, '*CTLIMGSAVE')
    tm.sleep(3)
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
        f.read(358)
        img = np.fromstring(f.read(area[0] * area[1] * 4), dtype=np.int).reshape(area[0], area[1])
    os.remove(data_file)
    print(img.max())
    #img[img < 0] = 0
    #img = img[10:,:]
    return img, t_expos

def main():

    main = MainWindow()
    main.show()

    main.pathBox.setText('X:/gonta/CloudData-2019/first_test_m2/Expanse_space/2/')
    main.nameBox.setText('name file')

    timer = QtCore.QTimer()


    def start():
        sendCommand(fileHandle, '*CTLSTART')
        timer.start(1)

    def stop():
        sendCommand(fileHandle, '*CTLSTOP')
        shutil.rmtree('Z:/Documents/Gentec-EO', ignore_errors=True)
        timer.stop()


    def save():
        global image
        np.savez_compressed(main.pathBox.text() + main.nameBox.text() + '.npz', a=image)
        #read -- loaded = np.load(main.pathBox.text() + main.nameBox.text() + '.npz')['a']

    def m2():
        global m2_flag, numStep, gera, pos
        if pos < 100:
            tl.test_move(device_id, tl.pos(0), 0)
            tl.test_wait_for_stop(device_id, 100)
            numStep = 0
            gera = True
        if pos > 100:
            tl.test_move(device_id, tl.pos(200), 0)
            tl.test_wait_for_stop(device_id, 100)
            numStep = len(lenght) - 1
            gera = False
        m2_flag = True



    global m2_flag, pos, gera, device_id
    m2_flag = False
    lenght = np.array([0, 20, 40, 50, 60, 70, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 160, 180, 200])
    device_id = tl.main()
    #tl.follow_home(device_id)
    tl.test_set_speed(device_id, 1024)
    pos, upos = tl.test_get_position(device_id)
    pos = int(pos * 2.56e-3)#round(pos * 2.56e-3, 0)

    def update():
        global image, m2_flag, device_id, numStep, gera

        saturation_level = int(str(sendCommand(fileHandle, '*MEAPKSAT'))[2:4])
        if saturation_level < 90 and saturation_level > 80:
            if m2_flag == True:
                image, t_expos = grab_image()
                position, upos = tl.test_get_position(device_id)
                position = int(position * 2.56e-3)#round(pos * 2.56e-3, 0)

                np.savez_compressed(main.pathBox.text() + str(2*lenght[numStep]) + '.npz', a=image)
                sendCommand(fileHandle, '*CTLSTART')
                if gera == True:
                    numStep += 1
                    if numStep == len(lenght):
                        m2_flag = False
                        numStep -= 1
                    tl.test_move(device_id, tl.pos(lenght[numStep]), 0)
                    tl.test_wait_for_stop(device_id, 100)
                    tm.sleep(2)

                else:
                    numStep -= 1
                    if numStep == -1:
                        m2_flag = False
                        numStep += 1
                    tl.test_move(device_id, int(tl.pos(lenght[numStep])), 0)
                    tl.test_wait_for_stop(device_id, 100)
                    tm.sleep(2)

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
