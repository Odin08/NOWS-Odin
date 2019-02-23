import numpy as np
import matplotlib.pyplot as plt
import struct
import os

import sys
# sys.path.append('X:/gonta/CloudData-2019/Programming/General scripts')
import M2_module as MM

path = 'X:/gonta/CloudData-2019/first_test_m2/despecl/'

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


# d = load_bmg('X:/gonta/CloudData-2019/background Beamage/background.bmg')


l = []
for i in os.listdir(path):
    l.append(int(i[:-4]))
l = np.array(l)
l.sort()

for i in l:
    data = (np.load(path + str(i) + '.npz')['a']).astype(float)
    print(np.mean([np.mean(data[0:10, :]), np.mean(data[:, 0:10])]))
    bl = np.mean([np.mean(data[0:10, :]), np.mean(data[:, 0:10])])
    #data = data - d
    data = data - bl
    data[data < 50] = 0
    #data = MM.Nominal(data, point=40)

    A = MM.Field_image(data)
    data = MM.window(data, A.x0, A.y0)
    #plt.imshow(data, cmap='nipy_spectral')
    #plt.show()
    #data_arr.append(data)
    a = MM.Field_image(data)
    w.append((a.w('x', 'HW') + a.w('y', 'HW'))/2.)
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
