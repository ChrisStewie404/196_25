import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# raw version of Lotka-volterra
def lotkafunc(v,t,params):
    x=v[0]
    y=v[1]
    alpha,beta,gamma,delta=params
    dxdt=alpha*x-beta*x*y
    dydt=-gamma*y+delta*x*y
    dvdt=[dxdt, dydt]
    return dvdt

# Competition Lotka-Volterra
def lotkacompfunc(v,t,params):
    x1,x2=v
    K1,K2,r1,r2,a12,a21=params
    dx1dt=r1*x1*(1-(x1+a12*x2)/K1)
    dx2dt=r2*x2*(1-(x2+a21*x1)/K2)
    dvdt=[dx1dt,dx2dt]
    return dvdt

# Ecosys Lotka-Volterra (competition + mutualism)
def lotkaecofunc(v,t,params):
    
    return dvdt
# alpha=4
# beta=1
# gamma=2
# delta=3
# params=[alpha,beta,gamma,delta]
K=[500,2000]
r=[0.5,0.5]
a=[0.7,0.3]
params=np.hstack((K,r,a))
y0=[50,200]
t=np.linspace(0,100,100)
sol=odeint(lotkacompfunc,y0,t,args=(params,))


plt.plot(t,sol[:,0],'b',label=' x(t)')
plt.plot(t,sol[:,1],'g',label='y(t)')
plt.legend(loc='best')
plt.grid()
plt.show()
