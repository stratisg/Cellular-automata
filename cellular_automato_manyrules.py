import numpy as np
import matplotlib.pyplot as plt

def cell_rule(num, neigh, x, index, sz):
    '''
    The cellular automato governing rule.
    '''
    data=[x[(index+k)%sz] for k in range(-neigh, neigh+1)] 
    data=np.array(data)
    rule=[]
    digits=2**(2*neigh+1)-1
    exp=[2**i for i in range(2*neigh, -1, -1)]
    exp=np.array(exp)
    for i in range(digits, -1, -1):
        rule.append(num//2**i)
        num=num%(2**i)
    ind=int(np.sum(exp*data))
    a=rule[digits-ind]
    return a

sz=int(input('Provide the length of the first chain:\n'))
ic=int(input('Provide the initial condition for the first chain. Choose from 0-%d:\n' %2**sz))
neigh=int(input('Provide the number of nearest neighbors who can influence your state for the first chain:\n'))
num=int(input('Provide the number of the rule you would like to use for the first chain. Choose from 0-%d:\n' %(2**(2**(2*neigh+1))-1))) # Rule we are going to use
x=[]
for i in range(sz-1, -1, -1): 
    x.append(ic//2**i)
    ic=ic%(2**i) 
x=np.array(x)
sz2=int(input('Provide the length of the second chain:\n'))
ic2=int(input('Provide the initial condition for the second chain. Choose from 0-%d:\n' %2**sz))
neigh2=int(input('Provide the number of nearest neighbors who can influence your state for the second chain:\n'))
num2=int(input('Provide the number of the rule you would like to use for the second chain. Choose from 0-%d:\n' %(2**(2**(2*neigh+1))-1))) # Rule we are going to use
x2=[]
for i in range(sz2-1, -1, -1): 
    x2.append(ic2//2**i)
    ic2=ic2%(2**i) 
x2=np.array(x2)
x=np.append(x, x2)
size=np.arange(sz+sz2)
tmax=int(input('Provide number of total steps the automaton will run for:\n'))
t=np.linspace(0,tmax, tmax+1)
plt.plot(size, x, '.')
y=x
data=[x]
for time in t[1::]:
    y1=[cell_rule(num, neigh, x, i, sz) for i in range(sz)]
    y2=[cell_rule(num2, neigh2, x, i, sz2) for i in range(sz, sz+sz2)]
    y1=np.array(y1)
    y2=np.array(y2)
    y=np.append(y1, y2)
    x=y
    plt.plot(size, x+time+1, '.')
    data.append(y)
plt.figure(2)
plt.imshow(data, cmap=plt.cm.binary)
plt.show()
