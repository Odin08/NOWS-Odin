#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
from matplotlib.pyplot import *
from scipy import ndimage
import numpy as np
from numpy.fft import rfft, ifft
# from scipy.optimize import least_squares
import scipy.optimize as opt
import scipy as sc
import matplotlib.pyplot as plt
from numpy import unravel_index
import time
import numba


pixel = 5.5e-3


def sizeBeam_approxi(arr):
    mas = wapp(arr)
    w = mas[0]
    return np.abs(w*pixel*np.sqrt(2))

def intensity(xdata_tuple, w, I, x0, y0, delta):
    global X
    x, y = xdata_tuple
    #s = time.time()
    ro = (X[None, :] - x0)**2 + (X[:, None] - y0)**2
    Eth = I * np.exp( - ro / w ** 2) + delta
    #print(time.time() - s)
    return Eth.ravel()

grid = np.mgrid[0:2048, 0:2048]
X = np.arange(0, 2048)

def wapp(arr):
    global grid
    x, y = grid

    x0, y0 = unravel_index(arr.argmax(), arr.shape)
	print(x0,y0)
    I0 = arr.max()
    bl = np.mean(arr[:10, :10])
    #s = time.time()
    res, cov = opt.curve_fit(intensity, (x, y), arr.ravel(), p0=(363, I0, x0, y0, bl))
    #print(time.time() - s)
	print(res)
    return res


