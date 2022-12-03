import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def ret(n,n1):
    r = np.where(n > n1, 0, 1)
    return r
def circonv(x1,x2,L):
    N=max(len(x1),len(x2))
    if len(x1)>len(x2):
        for i in range(len(x2),len(x1)):
            x2.append(0)
    else:
        for i in range(len(x1),len(x2)):
            x1.append(0)

    temp_x1=[]
    temp_x1.append(x1[0])
    for i in range(1,len(x1)):
        temp_x1.append(x1[N-i])
    x1=temp_x1
    cycle_mat=[]
    cycle_mat.append(x1)
    for step in range(1,N):
        temp=[]
        for i in range(0,N):
            temp.append(0)
        for i in range(0,N):
            temp[(i+step)%N]=x1[i]
        cycle_mat.append(temp)
    cycle_mat=np.array(cycle_mat)
    x2=np.array(x2)
    result=np.dot(cycle_mat,np.transpose(x2))
    result=list(result)
    result=result[0:L]
    return result    

n=np.arange(0,5)
x1=(n+1)*ret(n,5)
x2=[2,5,4,3]
print(len(x1),len(x2))
y1=signal.convolve(x1,x2)
plt.subplot(121)
plt.stem(np.arange(len(x1)+len(x2)-1),y1)
plt.grid()
plt.subplot(122)
plt.stem(circonv(x1,x2,7))
plt.grid()
plt.show()