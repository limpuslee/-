import numpy as np
import matplotlib.pyplot as plt

print('Please input a number:')
sigma=0.1*(int(input()))
n=np.arange(-1,25)
x=np.exp((sigma+0.5j)*n)
plt.figure(figsize=(8,6))
plt.subplot(1,2,1)
plt.title("Real")
plt.ylim(-10,10) 
plt.xlabel("n") 
plt.stem(n,np.real(x))
plt.subplot(1,2,2)
plt.title("Imaginary")
plt.ylim(-10,10) 
plt.stem(n,np.imag(x))
plt.xlabel("n")
plt.show()