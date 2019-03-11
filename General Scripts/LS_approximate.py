# -*- coding: utf-8 -*-
#
from matplotlib.pyplot import *
from scipy import ndimage
import numpy as np
from numpy.fft import rfft, ifft
from scipy.optimize import least_squares
import scipy as sc
import matplotlib.pyplot as plt
from numpy import unravel_index


pixel = 5.5e-3

def field(w0, x0, y0, X, Y):
    X, Y = np.mgrid[0:X, 0:Y]
    ro = (X - x0)**2 + (Y - y0)**2
    I = 3500
    return I * np.exp( - ro / w0 ** 2)

def intensity(p, arr):
    print(arr)
    arr = arr.reshape(1024, 1024)
    #x = np.arange(0, 1024)
    #arr = (x[None, :]) ** 2 + (x[:, None]) ** 2
    #E = field(60., 346., 490., 1024, 1024)
    #E = E + 140
    #arr = E
    X = np.arange(0, arr.shape[0])
    w = p[0]
    I = p[1]
    x0 = p[2]
    y0 = p[3]
    delta = p[4]
    ro = (X[:, None] - x0)**2 + (X[None, :] - y0)**2
    Eth = I * np.exp( - ro / w ** 2) + delta
    return np.abs(np.sum(Eth - arr))

def wapp(arr):
    x0, y0 = unravel_index(arr.argmax(), arr.shape)
    X = np.arange(0, len(arr))
    I0 = arr.max()
    arr1 = np.reshape(arr, 1024*1024)
    #res =  sc.optimize.leastsq(intensity, [100., I0, x0, y0, 100], args=(arr1))
    res = least_squares(intensity, [100., I0, x0, y0, 100], args=(arr1,))
    return res.x

E = field(60., 346., 490., 1024, 1024)
E = E + 140
masx = wapp(E)
print(masx)
#print(intensity(masx))
'''
def fun_rosenbrock(x):
    return np.array([1+ (x[1] - x[0]**2), (1 - x[0])])

from scipy.optimize import least_squares
x0_rosenbrock = np.array([20, 20])
res_1 = least_squares(fun_rosenbrock, x0_rosenbrock)
print(res_1.x)

'''