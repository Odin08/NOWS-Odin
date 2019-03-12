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
import time
import numba

plt.nipy_spectral()

pixel = 5.5e-3


def sizeBeam_approxi(arr):
    mas = wapp(arr)
    w = mas[0]
    return np.abs(w*pixel*np.sqrt(2))

def field(w0, I, x0, y0, X, Y):
    X, Y = np.mgrid[0:X, 0:Y]
    ro = (X - x0)**2 + (Y - y0)**2
    return I * np.exp( - ro / w0 ** 2)

def intensity(p, arr):
    X, Y = np.mgrid[0:arr.shape[0], 0:arr.shape[1]]
    w = p[0]
    I = p[1]
    x0 = p[2]
    y0 = p[3]
    delta = p[4]
    ro = (X - x0)**2 + (Y - y0)**2
    Eth = I * np.exp( - ro / w ** 2) + delta
    l = Eth - arr
    l = np.reshape(l, arr.shape[0]*arr.shape[1])
    return l


def wapp(arr):
    x0, y0 = unravel_index(arr.argmax(), arr.shape)
    I0 = arr.max()
    bl = np.mean(arr[:10, :10])
    res = least_squares(intensity, [50., I0, x0, y0, bl], args=(arr,))
    return res.x

'''
E = field(60., 3500., 346., 490., 1024, 1024)
E = E + 140.
d = 200*np.random.rand(1024, 1024)
E = E + d

s = time.time()
print(sizeBeam_approxi(E))
print(time.time() - s)
'''