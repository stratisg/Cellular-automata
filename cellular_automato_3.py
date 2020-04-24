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

sz=int(input('Provide the length of the chain:\n'))
ic=int(input('Provide the initial condition. Choose from 0-%d:\n' %2**sz))
neigh=int(input('Provide the number of nearest neighbors who can influence your state:\n'))
x=[]
for i in range(sz-1, -1, -1): 
    x.append(ic//2**i)
    ic=ic%(2**i) 
x=np.array(x)
size=np.arange(sz)
tmax=int(input('Provide number of total steps the automaton will run for:\n'))
t=np.linspace(0,tmax, tmax+1)
plt.plot(size, x, '.')
y=x
data=[x]
num=int(input('Provide the number of the rule you would like to use. Choose from 0-%d:\n' %(2**(2**(2*neigh+1))-1))) # Rule we are going to use
for time in t[1::]:
    y=[cell_rule(num, neigh, x, i, sz) for i in range(sz)]
    x=y
    plt.plot(size, x+time+1, '.')
    data.append(y)
plt.figure(2)
plt.imshow(data, cmap=plt.cm.binary)
plt.show()
