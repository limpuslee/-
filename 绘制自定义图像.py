import numpy as np
import matplotlib.pyplot as plt

print("Input(0-10):")
n=(int(input()))
x=np.arange(0,40*n)
y=2*np.sin(0.2*np.pi*x)+3*np.sin(0.25*np.pi*x)
plt.figure(figsize=(12.8,7.2))
plt.title('3200432102')
plt.xlabel('n')
plt.stem(x,y)
plt.show()