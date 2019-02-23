# -*- coding: utf-8 -*-
#
from matplotlib.pyplot import *
from scipy import ndimage
import numpy as np
from numpy.fft import rfft, ifft
from scipy.optimize import least_squares
from scipy import integrate
import matplotlib.pyplot as plt


pixel = 5.5e-3# 6.45e-3 #5.3e-3#3.75e-3


def window(arr, x0, y0, RAMKA=300):
    x0 = int(x0)
    y0 = int(y0)
    arr = (arr[
            y0-RAMKA if y0>RAMKA else 0 : y0+RAMKA if y0+RAMKA<len(arr) else -1 ,
            x0-RAMKA if x0>RAMKA else 0 : x0+RAMKA if x0+RAMKA<len(arr[0]) else -1
            ]).astype(float)
    return arr

def Nominal(arr, point=0):
    #bl = np.mean(arr[0:10, 0:10])
    #bl = np.max([arr[0:10,0:10].max(),arr[-10:,-10:].max()])
    #arr = arr - bl - point
    #arr[arr < 0] = 0
    arr = arr - arr.min()
    arr[arr < point] = 0
    return arr

def r2(arr, center):
    dimy, dimx = arr.shape
    X, Y = np.mgrid[:dimx, :dimy]
    X = X.T
    Y = Y.T
    return np.sum(arr * (X - center[1]) ** 2) / np.sum(arr) + np.sum(arr * (Y - center[0]) ** 2) / np.sum(arr)

class Field_image:
    def __init__(self, data):
        self.data = data
        self.dimy, self.dimx = np.shape(self.data)
        X, Y = np.mgrid[0:self.dimx, 0:self.dimy]
        self.X = X.T
        self.Y = Y.T
        self.P = np.sum(self.data)
        self.x0 = np.sum(np.sum(self.data * self.X)) / self.P
        self.y0 = np.sum(np.sum(self.data * self.Y)) / self.P

    def Profile(self, axis):
        if axis == 'x':
            sign = +1
        elif axis == 'y':
            sign = -1
        arr = np.sum(self.data, axis=int((sign + 1)/2))
        arr = arr/arr.max()
        #arr = (arr - arr.min())/((arr - arr.min()).max())
        return arr
    
    def SecondMoment(self):
        return np.sum(self.data * (self.X - self.x0) ** 2) / self.P, np.sum(self.data * (self.Y - self.y0) ** 2) / self.P
        #return np.sum(self.data * (self.X - x0) ** 2) / self.P, np.sum(self.data * (self.Y - y0) ** 2) / self.P

    def Correlation_xy(self):
        return np.sum(self.data * (self.X - self.x0) * (self.Y - self.y0)) / self.P

    def angle(self):
        return 0.5 * np.arctan2(2 * self.Correlation() / (self.SecondMoment()[0] - self.SecondMoment()[1]))

    def gamma(self):
        return np.sign(self.SecondMoment()[0] - self.SecondMoment()[1])

    def w(self, axis, method='d4s', level=np.exp(-2)):
        #Выбор оси
        if axis == 'x':
            sign = +1
        elif axis == 'y':
            sign = -1
        #Выбор метода    
        if method == 'd4s':
            return pixel * np.sqrt(2) * (self.SecondMoment()[0] + self.SecondMoment()[1] + sign * self.gamma() * (
                    (self.SecondMoment()[0] - self.SecondMoment()[1]) ** 2 + 4 * self.Correlation_xy() ** 2) ** 0.5) ** 0.5
        #Half width    
        elif method == 'HW':
            # возвращает радиус пучка по exp(-1) по полю
            # вычисленный по заданному уровню
            arr = np.sum(self.data, axis=int((sign + 1)/2))
            arr /= max(arr)
            #arr = (arr - arr.min())/((arr - arr.min()).max())
            buff = []
            for i in range(len(arr) - 1):
                if (arr[i] <= level and arr[i + 1] > level) or (arr[i] >= level and arr[i + 1] < level):
                    k = -(arr[i] - arr[i + 1])
                    b = arr[i] - k * i
                    x = (level - b) / k
                    buff.append(x)
            if len(buff) > 1:
                return float((buff[-1] - buff[0]) / 2. * np.sqrt(-2. / np.log(level)))*pixel
            else:
                return 0#'Error'

def w_prof(arr, level=np.exp(-2)):
    arr = (arr - arr.min()) / ((arr - arr.min()).max())
    buff = []
    for i in range(len(arr) - 1):
        if (arr[i] <= level and arr[i + 1] > level) or (arr[i] >= level and arr[i + 1] < level):
            k = -(arr[i] - arr[i + 1])
            b = arr[i] - k * i
            x = (level - b) / k
            buff.append(x)
    if len(buff) > 1:
        return float((buff[-1] - buff[0]) / 2. * np.sqrt(-2. / np.log(level)))
    else:
        return 0  # 'Error'

def w2_theory(p, z):
    M2=p[0]
    w0=p[1]
    z0=p[2]
    #z0 = 95
    return w0*np.sqrt(1. + ((z-z0)*M2*1064e-6/(np.pi*w0**2))**2)

def M2(lenght, w2):
	res =  least_squares(lambda a,x,y: w2_theory(a,x)-y, [1., 190e-3, 100], args=(lenght, w2))
	return res.x

def xy_profile_ave(img):
    x_graph = np.sum(img, axis=0)
    y_graph = np.sum(img, axis=1)
    return x_graph/x_graph.max(), y_graph/y_graph.max()

def xy_profile(img, x0, y0):
    x_graph = img[y0, :]
    y_graph = img[:, x0]
    return x_graph, y_graph

def RingSum(center, array):
    arr = np.copy(array)
    I_phi = []
    dimx, dimy = arr.shape
    Y, X = np.ogrid[:dimx, :dimy]
    for i in range(0, dimx//2):
        distance_from_center = np.sqrt((X - center[1])**2 + (Y-center[0])**2)
        mask = (i <= distance_from_center) & (distance_from_center <= i)
        I_phi.append(np.mean(arr[mask]))
    r = np.arange(0, dimx//2)
    return I_phi, r

def CircleMask(center, radius, arr):
    dimx, dimy = arr.shape
    Y, X = np.ogrid[:dimx, :dimy]
    distance_from_center = np.sqrt((X - center[1])**2 + (Y-center[0])**2)
    mask = distance_from_center <= radius
    return mask



def f1(p, x):
    x0=p[0]
    w0=p[1]
    return np.exp(-((x - x0)**2/w0**2))

def drawCircle(x0, y0, r, array):#Bresenham's line algorithm
    x, y, delta, error = 0, r, 1 - 2 * r, 0
    arr = (np.copy(array)).astype(bool)
    arr[arr > -1] = False
    while y >= 0:
        arr[x0 + x, y0 + y] = True
        arr[x0 + x, y0 - y] = True
        arr[x0 - x, y0 + y] = True
        arr[x0 - x, y0 - y] = True
        error = 2 * (delta + y) - 1
        if (delta < 0) and (error <= 0):
            x += 1
            delta += 2 * x + 1
            continue
        if (delta > 0) and (error > 0):
            y -= 1
            delta -= 2 * y + 1
            continue
        x += 1
        delta += 2 * (x - y)
        y -= 1

    return arr
def R_average(x0, y0, rmax, arr):
    I_r = []
    r = np.arange(0, rmax, 1)
    for i in r:
        I0 = drawCircle(x0, y0, i, I)
        I_r.append(np.average(arr[I0]))
    return I_r



#data = np.array([[1, 2, 3], [4, 5, 6], [7, 3, 3]])
#print()
#A = Field_image(data/data.max())
#print(A.w_x('d4s', level=0.1))

'''
def w2_emper(arr, level):
    
    buff = []
    for i in range(len(arr) - 1):
        if (arr[i] <= level and arr[i+1] > level) or  (arr[i] >= level and arr[i+1] < level):
            k = -(arr[i] - arr[i+1])
            b = arr[i] - k * i
            x = (level - b)/k
            buff.append(x)
    if len(buff) > 1:
        return (buff[-1] - buff[0])/2.*pixel*np.sqrt(-2./np.log(level))
    else:
        return 0
'''
'''
def d4s(data):
    if data.max() > 0:
        dimy, dimx = np.shape(data)
        X, Y = np.mgrid[0:dimx, 0:dimy]
        X = X.T
        Y = Y.T
        P = np.sum(data)
        xx = np.sum(np.sum(data * X)) / P
        yy = np.sum(np.sum(data * Y)) / P
        xx2 = np.sum(data * (X - xx)**2) / P
        yy2 = np.sum(data * (Y - yy)**2) / P
        xy = np.sum(data * (X - xx) * (Y - yy)) / P
        gamm = np.sign(xx2 - yy2)
        angle = 0.5 * np.arctan(2*xy / (xx2 - yy2))
        try:
            rx = np.sqrt(2) * (xx2 + yy2 + gamm * ( (xx2 - yy2)**2 + 4*xy**2)**0.5)**(0.5)
            ry = np.sqrt(2) * (xx2 + yy2 - gamm * ( (xx2 - yy2)**2 + 4*xy**2)**0.5)**(0.5)
        except:
            # In case of error, just make the size very large
            print ("Fitting error")
            rx, ry = data.shape
        return int(xx), int(yy), rx, ry, angle, xx2 + yy2
    else:
        return 0,0,0,0,0,0
'''

'''
x = np.arange(0, 400, 1.)
y = np.arange(0, 400, 1.)
I = np.exp(-((x[:, None] - 200)**2 + (y - 200)**2)/1600)
I /= np.sum(I)
x0, y0 = 200, 200


plot(I[200, -200:], 'o',label='Theory')
#I1 = R_average(x0, y0, 198, I)
I2, r = RingSum((x0, y0), I)
print(2*np.pi*np.sum(I2))

#plot(I1, label='Bresenhams line algorithm')
plot(I2, label='Mine method')

legend()
grid()
show()
'''



