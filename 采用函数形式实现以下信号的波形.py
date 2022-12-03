import numpy as np
import matplotlib.pyplot as plt


n=np.arange(-6,14,1)
def seqshift(x,m):
    x=x-m
    return x
interval1 = [1 if(i>=-2 and i<0) else 0 for i in n]
interval2 = [1 if(i>=0 and i<4) else 0 for i in n] 
interval3 = [1 if(i>=4 and i<8) else 0 for i in n]
def Y(num):
    y=interval1*(-4-2*num)+interval2*(-4+3*num)+interval3*(16-2*num)
    return y

plt.figure(figsize=(12.8,7.2)) 
plt.subplot(1,3,1)
plt.title('Piecewise Function x(n)')
plt.stem(n,Y(n))
plt.subplot(1,3,2)
plt.title('Piecewise Function x(n+3)')
plt.stem(n,Y(seqshift(n,3)))
plt.subplot(1,3,3)
plt.title('Piecewise Function x(-n-3)')
plt.stem(n,-1*Y(seqshift(n,3)))
plt.show()