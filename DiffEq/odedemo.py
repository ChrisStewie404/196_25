import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pend(y,t,b,c):
    theta,omega=y
    dydt=[omega,-b*omega-c*np.sin(theta)]
    return dydt

b=0.25
c=5
y0=[np.pi-0.1,0.0]
t=np.linspace(0,10,101)
sol=odeint(pend,y0,t,args=(b,c))
plt.plot(t,sol[:,0],'b',label=' theta(t)')
plt.plot(t,sol[:,1],'g',label=' omega(t)')
plt.legend(loc='best')
plt.grid()
plt.show()


# ode(var=1, order=n) --> ode(var=n, order=1) (first order vector)
# dy1/dt=f1(y1,y2,yn,t)
# dy2/dt=f2(y1,y2,yn,t)
# .
# .
# .
# dyn/dt=fn(y1,y2,yn,t)



# odeint(func,y0,t)

# func(y,t) (if func(t,y), then set tfirst=True)
# NOTE: func(y,t) must not modify the value of y

# y0 stores the inital value of the equation (SHOULD NOT BE MODIFIED BY func()!!!)

