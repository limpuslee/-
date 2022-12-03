import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
N, Wn = signal.buttord([20, 50], [14, 60], 3, 40, True)
b, a = signal.butter(N, Wn, 'band', True)
w, h = signal.freqs(b, a, np.logspace(1, 2, 500))
plt.semilogx(w, 20 * np.log10(abs(h)))  # 用于绘制折线图，两个函数的 x 轴、y 轴分别是指数型的，并且转化为分贝
plt.title('Butterworth bandpass filter fit to constraints')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')  # 显示网格
plt.fill([1,  14,  14,   1], [-40, -40, 99, 99], '0.9', lw=0)  # 区域颜色填充阻带
plt.fill([20, 20,  50,  50], [-99, -3, -3, -99], facecolor='gray', alpha=0.2) # 通带，[x_左下, x_左上,  x_右上, x_右下(左下角顺时针)], [y_左下, y_左上,  y_右上, y_右下]
plt.fill([60, 60, 1e9, 1e9], [99, -40, -40, 99], '0.9', lw=0)  # 阻带
plt.axis([10, 100, -60, 3])  # 画布大小
plt.show()
