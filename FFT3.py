import numpy as np
import matplotlib.pyplot as plt


a = 2
fs = 200
n = np.arange(0, 5/a/10, 1/fs)
xn = np.cos(2*np.pi*10*a*n)
xk = abs(np.fft.fft(xn))
yn = xn + np.random.rand(len(n))
yk = abs(np.fft.fft(yn))


plt.subplot(221)
plt.stem(xn)
plt.xlabel('xn')
plt.subplot(222)
plt.stem(yn)
plt.xlabel('yn')
plt.subplot(223)
plt.stem(xk)
plt.xlabel('xk')
plt.subplot(224)
plt.stem(yk)
plt.xlabel('yk')
plt.show()