from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

num = np.array([1, 0.35, -0.8])
den = np.array([2.5, -1.8, 0])
n = np.arange(0, 10)
tout, hout = signal.dimpulse((num, den, 1), len(n))
#时不变
x1 = n*np.where(n >= 0, 1, 0)
x2 = (n-1)*np.where(n >= 0, 1, 0)

y1 = signal.convolve(x1-1, np.squeeze(hout), mode='same')
y2 = signal.convolve(x2, np.squeeze(hout), mode='same')
#线性
x3=x1+x2
y3=signal.convolve(x3,np.squeeze(hout),mode='same')
plt.subplot(2, 2, 1)
plt.stem(n, y1)
plt.grid()
plt.xlabel('y1')
plt.subplot(2, 2, 2)
plt.stem(n, y2)
plt.grid()
plt.xlabel('y2')
plt.subplot(2,2,3)
plt.stem(n,y1+y2)
plt.grid()
plt.xlabel('y3')
plt.subplot(2,2,4)
plt.stem(n,y3)
plt.grid()
plt.xlabel('y1+y2')
plt.show()