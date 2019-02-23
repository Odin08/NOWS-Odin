import numpy as np
import matplotlib.pyplot as plt


def ln(f):
    return np.array([[1., 0.], [-1. / f, 1.]])


def tr(d):
    return np.array([[1., d], [0., 1.]])


def ABCD(mat):
    l = len(mat)
    matrix = mat[-1]
    for i in np.arange(2, l + 1):
        matrix = np.dot(matrix, mat[-i])
    return matrix


class ABCD_q:
    def __init__(self, ABCD, W0):
        Q0 = -1j * np.pi * W0 ** 2 / 1064e-6
        self.q = (ABCD[0, 0] * Q0 + ABCD[0, 1]) / (ABCD[1, 0] * Q0 + ABCD[1, 1])
        self.w0 = np.sqrt(abs(1064e-6 * self.q.imag / np.pi))
        self.q0 = 1j*self.q.imag
        self.z = self.q.real
        self.w = np.sqrt(1064e-6/np.pi/abs((1/self.q).imag))

# z, w0m, zr = [], [], []
# d = np.arange(-1, 1, 0.01)
# for i in d:
#    m = ABCD([tr(i + 3.86), ln(3.86), tr(70), ln(100)])
#    q1 = q(m, q0(11e-3))
#    z.append(Pos_w0(q1)[0])
#    w0m.append(Pos_w0(q1)[1])
#    zr.append(abs(q0(Pos_w0(q1)[1])))
# plt.plot(d, z)
# plt.xlabel('delta, mm')
# plt.ylabel('W0, mm')
# plt.grid()
# plt.show()

'''
wo = np.arange(0.025, 0.1, 0.01)

z1 = np.sqrt(0.2**2/wo**2 - 1)*np.pi*wo**2/1064e-6
z2 = np.sqrt(0.8**2/wo**2 - 1)*np.pi*wo**2/1064e-6 - 100
plt.plot(wo*1000, z1)
plt.plot(wo*1000, z2)
plt.grid()
plt.xlabel('w0, mm')
plt.ylabel('delta, mm')
plt.show()

d = np.arange(-3, 3, 0.01)
q00 = q0(11e-3)
q = (q00 + 4. + d)/(-q00/4. - d/4.)
plt.plot(d, np.sqrt(abs(1064e-6 * q.imag / np.pi)))
plt.show()
'''
