import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
b, a = signal.cheby1(4, 5, 100, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Chebyshev Type I frequency response (rp=5)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)  # 去除画布四周白边
plt.grid(which='both', axis='both')
plt.axvline(100, color='green')  # # 绘制竖线，低通临界频率为100Hz
plt.axhline(-5, color='green')  # 绘制横线-rp
plt.show()
