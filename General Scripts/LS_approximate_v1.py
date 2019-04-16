# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import least_squares
from numpy import unravel_index
import numba

pixel = 5.5e-3


def sizeBeam_approxi(arr):
    mas = wapp(arr)
    print(mas)
    w = mas[0]
    return np.abs(w*pixel)

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

@numba.jit(nopython=True, parallel=True)#("float64[:](float64[:,:,:,:,:], float64[:,:])")
def Field(p, arr):
    w = p[0]
    I = p[1]
    x0 = p[2]
    y0 = p[3]
    delta = p[4]
    ar = np.copy(arr)
    for i in numba.prange(0, arr.shape[0]):
        for j in numba.prange(0, arr.shape[1]):
            ar[i][j] = I * np.exp(-2*((i - x0) ** 2 + (j - y0) ** 2) / w ** 2) + delta - arr[i][j]
    return ar.ravel()


def wapp(arr):
    x0, y0 = unravel_index(arr.argmax(), arr.shape)
    I0 = arr.max()
    bl = np.mean(arr[:10, :10])
    res = least_squares(Field, [100., I0, x0, y0, bl], args=(arr,))
    return res.x

