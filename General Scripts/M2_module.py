# -*- coding: utf-8 -*-
#
from matplotlib.pyplot import *
from scipy import ndimage
import numpy as np
from numpy.fft import rfft, ifft
from scipy.optimize import least_squares
from scipy import integrate
import matplotlib.pyplot as plt


pixel = 5.5e-3# 6.45e-3 #5.3e-3#3.75e-3


def window(arr, x0, y0, RAMKA=300):
    x0 = int(x0)
    y0 = int(y0)
    arr = (arr[
            y0-RAMKA if y0>RAMKA else 0 : y0+RAMKA if y0+RAMKA<len(arr) else -1 ,
            x0-RAMKA if x0>RAMKA else 0 : x0+RAMKA if x0+RAMKA<len(arr[0]) else -1
            ]).astype(float)
    return arr

def Nominal(arr, point=0):
    #bl = np.mean(arr[0:10, 0:10])
    #bl = np.max([arr[0:10,0:10].max(),arr[-10:,-10:].max()])
    #arr = arr - bl - point
    #arr[arr < 0] = 0
    arr = arr - arr.min()
    arr[arr < point] = 0
    return arr

def r2(arr, center):
    dimy, dimx = arr.shape
    X, Y = np.mgrid[:dimx, :dimy]
    X = X.T
    Y = Y.T
    return np.sum(arr * (X - center[1]) ** 2) / np.sum(arr) + np.sum(arr * (Y - center[0]) ** 2) / np.sum(arr)

class Field_image:
    def __init__(self, data):
        self.data = data
        self.dimy, self.dimx = np.shape(self.data)
        X, Y = np.mgrid[0:self.dimx, 0:self.dimy]
        self.X = X.T
        self.Y = Y.T
        self.P = np.sum(self.data)
        self.x0 = np.sum(np.sum(self.data * self.X)) / self.P
        self.y0 = np.sum(np.sum(self.data * self.Y)) / self.P

    def Profile(self, axis):
        if axis == 'x':
            sign = +1
        elif axis == 'y':
            sign = -1
        arr = np.sum(self.data, axis=int((sign + 1)/2))
        arr = arr/arr.max()
        #arr = (arr - arr.min())/((arr - arr.min()).max())
        return arr
    
    def SecondMoment(self):
        return np.sum(self.data * (self.X - self.x0) ** 2) / self.P, np.sum(self.data * (self.Y - self.y0) ** 2) / self.P
        #return np.sum(self.data * (self.X - x0) ** 2) / self.P, np.sum(self.data * (self.Y - y0) ** 2) / self.P

    def Correlation_xy(self):
        return np.sum(self.data * (self.X - self.x0) * (self.Y - self.y0)) / self.P

    def angle(self):
        return 0.5 * np.arctan2(2 * self.Correlation() / (self.SecondMoment()[0] - self.SecondMoment()[1]))

    def gamma(self):
        return np.sign(self.SecondMoment()[0] - self.SecondMoment()[1])

    def w(self, axis, method='d4s', level=np.exp(-2)):
        #Выбор оси
        if axis == 'x':
            sign = +1
        elif axis == 'y':
            sign = -1
        #Выбор метода    
        if method == 'd4s':
            return pixel * np.sqrt(2) * (self.SecondMoment()[0] + self.SecondMoment()[1] + sign * self.gamma() * (
                    (self.SecondMoment()[0] - self.SecondMoment()[1]) ** 2 + 4 * self.Correlation_xy() ** 2) ** 0.5) ** 0.5
        #Half width    
        elif method == 'HW':
            # возвращает радиус пучка по exp(-1) по полю
            # вычисленный по заданному уровню
            arr = np.sum(self.data, axis=int((sign + 1)/2))
            arr /= max(arr)
            #arr = (arr - arr.min())/((arr - arr.min()).max())
            buff = []
            for i in range(len(arr) - 1):
                if (arr[i] <= level and arr[i + 1] > level) or (arr[i] >= level and arr[i + 1] < level):
                    k = -(arr[i] - arr[i + 1])
                    b = arr[i] - k * i
                    x = (level - b) / k
                    buff.append(x)
            if len(buff) > 1:
                return float((buff[-1] - buff[0]) / 2. * np.sqrt(-2. / np.log(level)))*pixel
            else:
                return 0#'Error'

def w_prof(arr, level=np.exp(-2)):
    arr = (arr - arr.min()) / ((arr - arr.min()).max())
    buff = []
    for i in range(len(arr) - 1):
        if (arr[i] <= level and arr[i + 1] > level) or (arr[i] >= level and arr[i + 1] < level):
            k = -(arr[i] - arr[i + 1])
            b = arr[i] - k * i
            x = (level - b) / k
            buff.append(x)
    if len(buff) > 1:
        return float((buff[-1] - buff[0]) / 2. * np.sqrt(-2. / np.log(level)))
    else:
        return 0  # 'Error'

def w2_theory(p, z):
    M2=p[0]
    w0=p[1]
    z0=p[2]
    #z0 = 95
    return w0*np.sqrt(1. + ((z-z0)*M2*1064e-6/(np.pi*w0**2))**2)

def M2(lenght, w2):
	res =  least_squares(lambda a,x,y: w2_theory(a,x)-y, [1., 100e-3, 125], args=(lenght, w2))
	return res.x

def xy_profile_ave(img):
    x_graph = np.sum(img, axis=0)
    y_graph = np.sum(img, axis=1)
    return x_graph/x_graph.max(), y_graph/y_graph.max()

def xy_profile(img, x0, y0):
    x_graph = img[y0, :]
    y_graph = img[:, x0]
    return x_graph, y_graph




