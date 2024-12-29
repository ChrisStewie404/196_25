import numpy as np

A=np.array(eval(input("请输入母序列和子序列：")))
X_mean=A/np.mean(A,axis=0)
X0=X_mean[:,0]  ## 母序列
Xi=X_mean[:,1:] ## 子序列
n,m=Xi.shape
abs_X=abs(Xi-np.tile(X0.reshape(-1,1),(1,m)))
rho=0.5         ## \rho默认值为0.5
a=np.min(np.min(abs_X))
b=np.max(np.max(abs_X))
kesi=(a+rho*b)/(abs_X+b)
r=np.mean(kesi,0)
print("raw r:\n{}".format(r))
sorted_r=np.sort(r)
sorted_idx=np.argsort(r)
print("sorted r:\n{}".format(sorted_r))
print("sorted index:\n{}".format(sorted_idx))
# print(X_mean)
# e.g
# (input)
# >>>[[1,2,3],[0,1,2],[4,5,6]]
# (output)
# >>>[1.66666667 2.66666667 3.66666667]