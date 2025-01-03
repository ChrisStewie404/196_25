# Grey Relation Analysis(GRA)
## introduction
**黑**: 无信息  
**白**: 完全已知(数据 & 关系)  
**灰**: 部分已知

GRA 旨在解决 **关联分析** 和 **多目标决策**

GRA 定义 **理想数据集(ideal data sets)** $$ X_0=[ X_0(1),X_0(2),\ldots,X_0(n) ]$$
和 **选择数据集(alternative data sets)** $$ X_k=[X_k(1),X_k(2),\ldots,X_k(n) ] \\ k=1,2,\ldots,m$$  
## 关联分析
对于每个指标，我们首先将其分别除以各自的均值，得到指标 $ Z_k \ k=0,1,2,\ldots,n$ 即  
$$Z_k=\frac{1}{\overline{X_k}}[X_k(1),X_k(2),\ldots,X_k(n) ]$$
我们定义
$$a=\ min_k \ min_j \ |Z_0(j) - Z_k(j)|$$  
$$b=\ max_k \ max_j \ |Z_0(j) - Z_k(j)|$$  
$$\xi_k(j)=\frac{a+\rho  b}{|Z_0(j) - Z_k(j)|+\rho  b} \ (<1 )$$  
这里 $\rho$ 是个超参数，通常取0.5  
指标 $X_0$ 和 $X_k$ 的相关系数 $ r_k$ 为  
$$ \frac{1}{n} \sum^{n}_{j=1} \xi_k(j)$$

## 决策  
决策和关联分析最大的区别在于，决策过程中我们**没有理想数据集 $X_0$** ,需要我们自己去构造，以下是构造方法：  
- 对于每个 **数据集的每个维度** （而不是 **数据集**），除以相应的均值，即  
$$ Z_k(j)=\frac{m*X_k(j)}{\sum^m_{l=1}X_l(j)}$$   
-  对于数据集的每个维度，我们都取最大值，即可得到完美数据集 $ Z_0, (\forall \ 1\le t \le m, Z_0(t)=max\{Z_k(t) \ | \ 1\le k \le n \} )$  
-  计算相关系数步骤同上  
- 最后得到相关系数最大的即为最优解  
## 推广版决策（多目标） 
在之前计算相关系数 $ r_k$ 时，我们具使用算术平均，为了突出我们想要研究的对象的重要性，可以修改权重，即
$$ r_k = \sum^{m}_{j=1} w(j) \times \xi_k(j)$$  
其中，$w(j)$ 为自定义参数




