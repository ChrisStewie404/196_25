import numpy as np
import matplotlib.pyplot as plt
import math

class GMpred:
    def __init__(self):
        self.a=0
        self.b=0
        self.X0=0
        self.X1=0
    
    def fit(self,X):
        n=len(X)
        self.X0=X
        self.X1=np.cumsum(X)
        Z=0.5*(self.X1[1:]+self.X1[:-1])
        Y=self.X0[1:]
        B=np.vstack((-Z,np.ones(n-1))).T
        Bsqr=np.dot(B.T,B)
        self.a,self.b=np.dot(np.linalg.inv(Bsqr),np.dot(B.T,Y))

    def predict(self,n):
        X_cpred=np.zeros(n)
        X_cpred[0]=self.X0[0]
        for i in range(1,n):
            #   X_cpred[i]=(self.b+X_cpred[i-1])/(1.0+self.a)
              X_cpred[i]=(self.X0[0]-self.b/self.a)*math.exp(-self.a*(i))+self.b/self.a
        X_pred=np.zeros(n)
        X_pred[0]=self.X0[0]
        for i in range(1,n):
            X_pred[i]=X_cpred[i]-X_cpred[i-1]
        return X_pred

# demo1    
X=np.array([20,25,30,35,40,45])
m=3
gm=GMpred()
gm.fit(X)
X_pred=gm.predict(m+len(X))

plt.plot(range(len(X)),X,'o-',label='Original')
plt.plot(range(len(X)+m),X_pred,'x--',label='Prediction')
plt.legend()
plt.show()