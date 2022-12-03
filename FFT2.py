import numpy as np
import matplotlib.pyplot as plt


a = 2
fs = 50
n = np.arange(0, 5/a/2, 1/fs)
xn = np.cos(2*np.pi*10*a*n) + np.cos(2*np.pi*20*n)
xk = abs(np.fft.fft(xn))


plt.subplot(211)
plt.stem(xn)
plt.subplot(212)
plt.stem(xk)
plt.show()