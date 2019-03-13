import numpy as np
import struct
import os
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
import sys
#sys.path.append('path')
import M2_module as MM

path = r"X:\gonta\CloudData-2019\first_test_m2\despecl_grinfilter_new\1"

lenght = range(0, 190, 20)
data_arr = []
w = []
j = 1


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


d = load_bmg('X:/gonta/CloudData-2019/first_test_m2/despecl_grinfilter_new/bl-30ms.bmg')
#d = d[2:, :]


l = []
for i in os.listdir(path):

    l.append(int(i[:-4]))
l = np.array(l)
l.sort()
k = 0
for i in l:
    data = (np.load(path + "/" + str(i) + '.npz')['a']).astype(float)
    #data = data[2:, :]
    data = data - d
    data[data < 0] = 0
    #data = data[10:, :]
    data = MM.window(data, 512, 512, RAMKA=300)
    datax = np.sum(data, axis=0)
    datay = np.sum(data, axis=1)
    masx = wapp(datax)
    masy = wapp(datay)
    plt.plot(datax)
    plt.plot(datay)
    plt.plot(intensity(masx, np.arange(0, len(datax))))
    plt.plot(intensity(masy, np.arange(0, len(datay))))
    plt.show()
    #data = MM.window(data, 512, 512, 350)
    #aver = (np.average(data[0:10, :]) + np.average(data[:, 0:10]))/2.
    #data = data - aver
    #data[data < 20] = 0

    #A = MM.Field_image(data)
    #data = MM.window(data, A.x0, A.y0)
    #plt.subplot( 3, 10, k)
    #plt.imshow(np.log10(data), cmap='nipy_spectral')
    #plt.plot(np.sum(data, axis=1)/700.)
    #plt.show()
    #data_arr.append(data)
    #a = MM.Field_image(data)
    w.append(masx[0]/2. + masy[0]/2.)

l.astype(float)
m2 = MM.M2(l, w)
ll = np.arange(0, 201, 0.1)
plt.plot(l, w, 'o')
plt.plot(ll, MM.w2_theory(m2, ll))
plt.grid()
plt.show()
print(m2)

'''
for i in lenght:
    data = np.load(path + '1/' + str(i) + '.0.npz')['a']
    data -= data.min()
    data = data/data.max()
    plt.subplot(3, 4, j)
    prof = data.sum(axis=0)
    prof = prof - prof.min()
    prof = prof/prof.max()*100
    plt.plot([0, len(prof) - 1],[13.5, 13.5])
    plt.plot(prof)

    d.append(data)
    a = MM.Field_image(data)
    w.append((a.w('x', 'HW') + a.w('y', 'HW'))/2)
    j += 1
'''
