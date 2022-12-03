import numpy as np
import matplotlib.pyplot as plt

def impulse(n0):
    y=np.where(n0>=2,0.0,1.0)
    return y

x=np.arange(0,15)


plt.figure(figsize=(6.4,4.8))
plt.title("Rectangle List")    
plt.ylim(0,1.2)
plt.stem(x,impulse(x))
plt.show()