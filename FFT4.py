import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def u(n):
    return np.where(n>=0,1,0)

a = 2
N = a+10
L = 20
n = np.arange(0,N,1)
x1 = np.array([1,3,2,4,6])
x2 = (n+2)*(u(n)-u(n-N))
x1 = np.pad(x1,(0,L-len(x1)),'constant', constant_values=(0,0))
x2 = np.pad(x1,(0,L-len(x2)),'constant', constant_values=(0,0))
xk1 = np.fft.fft(x1,L)
xk2 = np.fft.fft(x2,L)
yk = xk1*xk2
yn1 = np.fft.ifft(yk)
yn2 = signal.convolve(x1,x2)

plt.subplot(211)
plt.stem(yn1)
plt.xlim(0,20)
plt.subplot(212)
plt.stem(yn2)
plt.xlim(0,20)
plt.show()