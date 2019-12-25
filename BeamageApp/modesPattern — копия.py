# -*- coding: utf-8 -*-
import numpy as np
#from scipy.optimize import least_squares
from scipy.special import genlaguerre, jv
import matplotlib.pyplot as plt

import sys
import os
sys.path.append('./holoeye')
import time
import holoeye
global slm
slm = holoeye.SLMDisplay()

def getPhase(field):
    return np.arctan2(field.imag, field.real)
def inversBessel_1st(x):
    p = [-0.04079135,  1.18647628,  1.72041897, -0.00288109]
    return p[0]*x + p[1]*np.arcsin(p[2]*x + p[3]*x**2)
def Uaom(p, m, r0, x0, y0):
    x, y = np.mgrid[0:1080, 0:1920]
    ro = np.sqrt( (x-x0) ** 2 + (y-y0) ** 2) / r0 * np.sqrt(2)
    phi = np.arctan2(y-y0 , x-x0)
    res = ro ** abs(m) * genlaguerre(p, abs(m))(ro ** 2) * np.exp(-ro ** 2 / 2.)
    #res = res.astype("complex128")
    #res = res * np.exp(1j * m * phi)
    if m < 0:
        res = res * np.sin(abs(m) * phi)
    else:
        res = res * np.cos(abs(m) * phi)
    res /= abs(res).max()
    norm = 1/np.sqrt(np.sum(abs(res)**2))
    return res, norm
def setPhase(p, m, r0, x0=550, y0=1050):
    U, n = Uaom(p, m, r0, x0, y0)
    U = U.conjugate()
    koeff = 0.5815
    U = U * koeff
    res = inversBessel_1st(abs(U))
    phase = ((res * np.sin(freq + getPhase(U))/dphi + 1/2.) * 255).astype(np.uint8)
    slm.showData(phase)
    #slm.showPhasevalues(phase, phaseWrap=dphi)
    #data = np.digitize(phase, rt, right=False) / 255. * dphi

    return n

x, y = np.mgrid[0:1080, 0:1920]
freq = (  x - y )*120./1000.
while True:
    x0 = int(input()) + 0
    #phi = np.arctan2(y - 1050 , x-x0 )
    dphi = 3.64
    setPhase(0,0, 1100/8., x0=495, y0=545 )
    #slm.showPhasevalues( (1+np.sin(phi*5))*3.64/2., phaseWrap = dphi)
    time.sleep(1)
    slm.release()
slm.close()


