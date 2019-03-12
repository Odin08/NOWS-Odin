import numpy as np
import matplotlib.pyplot as plt
import struct
import os

import sys
#sys.path.append('path')
import M2_module as MM
import LS_approximate as ls
path = 'D:/Laboratory/CloudData-2019/first_test_m2/despecl_grinfilter_new/2/'

lenght = range(0, 190, 20)
data_arr = []
w = []
j = 1


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


d = load_bmg(r'D:\Laboratory\CloudData-2019\first_test_m2\despecl_grinfilter_new\bl-100ms.bmg')
d = d[2:, :]

l = []
for i in os.listdir(path):
    l.append(int(i[:-4]))
l = np.array(l)
l.sort()

for i in l:
    data = (np.load(path + str(i) + '.npz')['a']).astype(float)
    data = data[2:, :]
    data = data - d
    data[data < 0] = 0

    #data = MM.window(data, 512, 6)
    #plt.imshow(data, cmap='nipy_spectral')
    #plt.show()
    ww = ls.sizeBeam_approxi(data)
    print(ww)
    w.append(ww)
l.astype(float)
m2 = MM.M2(l, w)
ll = np.arange(0, 201, 0.1)
plt.plot(l, w, 'o')
plt.plot(ll, MM.w2_theory(m2, ll))
plt.grid()
plt.show()
print(m2)
