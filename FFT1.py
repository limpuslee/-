import numpy as np
import matplotlib.pyplot as plt


a = 2
f = 2
n = np.arange(0, a/f, 1/500)
xn= np.cos(2*np.pi*a*n)
xk = np.fft.fft(xn)


plt.subplot(211)
plt.stem(xn)
plt.subplot(212)
plt.stem(abs(xk))
plt.show()