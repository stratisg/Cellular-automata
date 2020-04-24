import numpy as np
import matplotlib.pyplot as plt

def cell_rule(num, x_l, x, x_r):
    '''
    The cellular automato governing rule.
    '''
    rule=[]
    for i in range(7, -1, -1):
        rule.append(num//2**i)
        num=num%(2**i)
    ind=4*x_l+2*x+x_r
    a=rule[ind]
    return a

side=100
size_l=int(side)
size_r=int(side)
sz=size_l+1+size_r
left=np.zeros(size_l, np.int32)
right=np.zeros(size_r, np.int32)
x=np.append(left, int(1))
x=np.append(x, right)
z=np.shape(x)[0]
size=np.arange(np.shape(x)[0])
tmax=2*int(side)
t=np.linspace(0,tmax, tmax+1)
plt.plot(size, x, '.')
y=x
data=[x]
num=int(input('Provide the number of the rule you would like to use:\n')) # Rule we are going to use
for time in t[1::]:
    y=[cell_rule(num, x[i-1], x[i], x[(i+1)%sz]) for i in range(sz)]
    x=y
    plt.plot(size, x+time+1, '.')
    data.append(y)
plt.figure(2)
plt.imshow(data, cmap=plt.cm.binary)
plt.show()
