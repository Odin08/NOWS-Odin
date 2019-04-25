import numpy as np
import struct
import os
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
import sys
import numba
import time
#sys.path.append('path')
import M2_module as MM
path = r"X:\gonta\CloudData-2019\Student\S1-5m"
import LS_approximate_v1 as ls

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
    return img

d = load_bmg(r'X:\gonta\CloudData-2019\Student\bl.bmg')


l = []
for i in os.listdir(path):
    l.append(int(i[:-4]))
l = np.array(l)
l.sort()
data_arr = []
for i in l:
    data = (np.load(path + "/" + str(i) + '.npz')['a']).astype(float)
    data = data - d
    data[data < 0] = 0
    data_arr.append(data)

def arr_w(data_arr):
    w = []
    for i in data_arr:
        s = time.time()
        ww = ls.sizeBeam_approxi(i)
        print(time.time() - s)
        w.append(ww)
    return w

w = arr_w(data_arr)
print(len(w), len(l))
l.astype(float)
m2 = MM.M2(l, w)
ll = np.arange(0, 401, 0.1)
plt.plot(l, w, 'o')
plt.plot(ll, MM.w2_theory(m2, ll))
plt.grid()
plt.show()
print(m2)
