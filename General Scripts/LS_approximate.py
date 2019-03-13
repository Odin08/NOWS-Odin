# -*- coding: utf-8 -*-
#
from matplotlib.pyplot import *
from scipy import ndimage
import numpy as np
from numpy.fft import rfft, ifft
from scipy.optimize import least_squares
from scipy import integrate
import matplotlib.pyplot as plt
from numpy import unravel_index
import numba


plt.nipy_spectral()

pixel = 5.5e-3

def field(w0, x0, y0, X, Y):
    X, Y = np.mgrid[0:X, 0:Y]
    ro = (X - x0)**2 + (Y - y0)**2
    I = 3500
    return I * np.exp( - ro / w0 ** 2)

def intensity(p, arr):
    X = np.arange(0, len(arr))
    w = p[0]
    I = p[1]
    x0 = p[2]
    delta = p[3]
    ro = (X - x0)**2
    return I * np.exp( - ro / w ** 2) + delta

def wapp(arr):
    x0 = arr.argmax()#unravel_index(arr.argmax(), arr.shape)
    X = np.arange(0, len(arr))
    I0 = arr.max()
    res =  least_squares(lambda a, x, array: intensity(a, x) - array, [100., I0, x0, 1000], args=(X, arr))
    return res.x
'''
#@numba.jit
def wapp(arr):
    Deff_arr = []
    Par = []
    x0, y0 = unravel_index(arr.argmax(), arr.shape)
    I0 = arr.max()
    w0 = 10.
    for i in np.arange(x0 - 20, x0 + 20):
        print(i)
        for j in np.arange(y0 - 20, y0 + 20):
            for kI in np.arange(I0 - 50, I0 + 50):
                for kw in np.arange(w0 - 10, w0 + 500):
                    E = intensity([kw, kI, i, j], arr)
                    Def = np.sum((E - arr)**2)
                    print(Def)
                    Deff_arr.append(Def)
                    Par.append([kw, kI, i, j])
    np.array(Deff_arr)
    res = Par[Deff.argmin()]
    print(res)
    return res
'''

def load_bmg(file):
    with open(file, 'rb') as f:
        f.read(8)
        s = f.read(8)
        area = np.fromstring(s, dtype=np.int32)
        f.read(20)
        f.read(8)
        f.read(41)
        f.read(4)
        f.read(358)
        img = np.fromstring(f.read(area[0] * area[1] * 4), dtype=np.int).reshape(area[0], area[1])
    #img = img[10:, :]
    return img

x = np.arange(0, 1024)
arr = (x[None, :])**2 + (x[:, None])**2
E = field(60., 346., 490., 1024, 1024)
d = load_bmg('X:/gonta/CloudData-2019/first_test_m2/despecl_grinfilter_new/bl-30ms.bmg')
E = E + d
#plt.imshow(E)
#plt.show()

Ex = np.sum(E, axis=0)
Ey = np.sum(E, axis=1)
masx = wapp(Ex)
masy = wapp(Ey)
plt.plot(Ex)
plt.plot(Ey)
plt.plot(intensity(masx, np.arange(0, len(Ex))))
plt.plot(intensity(masy, np.arange(0, len(Ey))))
plt.show()



