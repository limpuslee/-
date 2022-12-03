import numpy as np
import matplotlib.pyplot as plt

print("Input(0-10):")
n=np.arange(0,20)
m=(int(input()))
def seqshift(x):
    x=x-m
    return x
plt.subplot(1,2,1)
plt.title('Before SeqShift')
plt.stem(n,2*n)
plt.subplot(1,2,2)
plt.title('After SeqShift')
plt.stem(n,seqshift(n))
plt.show()