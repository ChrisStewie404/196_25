import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def logfunc(v,t,params):
    r,K,Q=params
    x=v
    dxdt=r*x(1-x/K)*Q
    return dxdt

# Q environment influence factor
# K capacity
# r growth rate
def logecofunc(v,t,r,K,A,Q):
    MC=np.dot(A,(v/K).T)
    MC=1-MC

    dvdt=v*MC
    dvdt=Q*r*dvdt
    return dvdt


t=np.linspace(0,100,1000)
y=[40,40,40,400]
K=[400,400,400,4000]
A=[[1,0.5,0.3,0.3],
   [-0.3,1,0.5,0.4],
   [0.2,0.7,1,0.2],
   [0.1,0.2,0.2,1]]
r=[0.4,0.3,0.5,0.6]
Q=1
sol=odeint(logecofunc,y,t,args=(r,K,A,Q))

plt.plot(t,sol[:,0],'b',label=' specie1')
plt.plot(t,sol[:,1],'g',label=' specie2')
plt.plot(t,sol[:,2],'r',label=' specie3')
plt.plot(t,sol[:,3],'o',label=' specie4')
plt.legend(loc='best')
plt.grid()
plt.show()
