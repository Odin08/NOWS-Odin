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
#slm = holoeye.SLMDisplay()
def initSLM():
    global slm
    slm = holoeye.SLMDisplay()

x, y = np.mgrid[0:1080, 0:1920]
X0 = 495
Y0 = 545

def Uaom(p, m, r0):
    x, y = np.mgrid[0:1080, 0:1920]
    ro = np.sqrt( (x-X0) ** 2 + (y-Y0) ** 2) / r0 * np.sqrt(2)
    phi = np.arctan2(y-Y0 , x-X0)
    res = ro ** abs(m) * genlaguerre(p, abs(m))(ro ** 2) * np.exp(-ro ** 2 / 2.)
    if m < 0:
        res = res * np.sin(abs(m) * phi)
    else:
        res = res * np.cos(abs(m) * phi)
    res /= abs(res).max()
    norm = 1/np.sqrt(np.sum(abs(res)**2))
    return res, norm

def U(p, m, r0):
    x, y = np.mgrid[-500:500, -500:500]
    ro = np.sqrt( (x) ** 2 + (y) ** 2) / r0 * np.sqrt(2)
    phi = np.arctan2(y, x)
    res = ro ** abs(m) * genlaguerre(p, abs(m))(ro ** 2) * np.exp(-ro ** 2 / 2.)

    if m < 0:
        res = res * np.sin(abs(m) * phi)
    else:
        res = res * np.cos(abs(m) * phi)
    norm = 1/np.sqrt(np.sum(abs(res)**2))
    return res*norm

dphi = 3.64

def getPhase(field):
    return np.arctan2(field.imag, field.real)
def inversBessel_1st(x):
    p = [-0.04079135,  1.18647628,  1.72041897, -0.00288109]
    return p[0]*x + p[1]*np.arcsin(p[2]*x + p[3]*x**2)
freq = ( - x - y )*180./1000.
def firstGenerate(r0):
    U, n = Uaom(0, 0, r0)
    koeff = 0.58
    U = U * koeff
    res = inversBessel_1st(abs(U))

    phase = res * np.sin(freq + getPhase(U)) + dphi/2.

    slm.showPhasevalues(phase, phaseWrap = dphi)
    time.sleep(1)

def setPhase(p, m, r0):
    U, n = Uaom(p, m, r0)
    U = U.conjugate()
    koeff = 0.5815
    U = U * koeff
    res = inversBessel_1st(abs(U))
    #phase = res * np.sin(freq + getPhase(U)) + dphi/2.
    #slm.showPhasevalues(phase, phaseWrap=dphi)
    phase = ((res * np.sin(freq + getPhase(U))/dphi + 1/2.) * 255).astype(np.uint8)
    slm.showData(phase)
    return n

def setPhase_cos(p, m, r0):
    U0, n0 = Uaom(0, 0, r0)
    U, n = Uaom(p, m, r0)

    Ufinal = U0.conjugate() + U.conjugate()
    NO = (abs(Ufinal)).max()
    koeff = 0.5815 / NO
    Ufinal = Ufinal * koeff#/abs(Ufinal).max() * 0.5479438511002689
    res = inversBessel_1st(abs(Ufinal))
    #phase = res * np.sin(freq + getPhase(Ufinal)) + dphi/2.
    #slm.showPhasevalues(phase, phaseWrap=dphi)
    phase = ((res * np.sin(freq + getPhase(Ufinal))/dphi + 1/2.) * 255).astype(np.uint8)
    slm.showData(phase)
    return NO

def setPhase_sin(p, m, r0):
    U0, n0 = Uaom(0, 0, r0)
    U, n = Uaom(p, m, r0)
    Ufinal = U0.conjugate() + U.conjugate() * 1j
    NO = (abs(Ufinal)).max()
    koeff = 0.5815 / NO
    Ufinal = Ufinal * koeff# / abs(Ufinal).max() * 0.5479438511002689
    res = inversBessel_1st(abs(Ufinal))
    #phase = res * np.sin(freq + getPhase(Ufinal)) + dphi/2.
    #slm.showPhasevalues(phase, phaseWrap=dphi)
    phase = ((res * np.sin(freq + getPhase(Ufinal)) / dphi + 1 / 2.) * 255).astype(np.uint8)
    slm.showData(phase)
    return NO

def closeSLM():
    slm.close()
def release():
    slm.release()

