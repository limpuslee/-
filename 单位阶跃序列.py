import numpy as np
import matplotlib.pyplot as plt
def stepseq(n0, n1, n2):
   if((n0 < n1) and (n0 > n2) and (n2 < n1)):
        print ("error")
   else:
       n=np.arange(n1,n2,1)
       x = (n-n0) >= 0 
       return x,n

x,n = stepseq(2, -6, 21)

plt.stem(n,x)  #离散序列作图函数
plt.xlabel('Time index n')
plt.ylabel('Amplitude')
plt.title('3200432102')
plt.axis([-5,20,0,1.2])
plt.show()