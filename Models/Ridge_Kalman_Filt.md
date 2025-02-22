
# B题潜水艇 2407038
## 潜水艇位置预测
1. ARIMA
2. 蒙特卡洛模拟
3. 岭回归
4. 微分方程  
   
## 搜索设备和搜索方案
1. 遗传算法
2. 网格搜索，贝叶斯

---

## ARIMA模型
见14周备赛文件

---

## 蒙特卡洛模拟


---

## 岭回归构建点坐标与洋流速度之间的函数关系  
回归类算法主要用于利用已知数据预测其他定量数据点  
专门用于处理多重共线性问题的线性回归改进算法，用于处理数据矩阵可能不是满秩的情况
### 建模流程  
1. 定义损失函数，通用 
$$L(\theta) = \sum_{i=1}^n(y_i-\sum_{i=1}^n\theta_j x_{ij})^2+\lambda \sum_{i=1}^n \theta_j^2$$
其中，$n$是样本数量，$m$是特征数量，$y_{i}$是第i个样本的目标值，$x_{ij}$是第i个样本的第j个特征值，$\theta _{j}$是第j个特征的权重，$\lambda$是正则化参数，控制正则化项的强度。当$\lambda$增大时，正则化项的影响增大，参数$\theta$趋向于较小的值，这有助于减少模型的复杂度和过拟合的风险。  
1. 参数估计，岭回归的参数估计可以通过最小化损失函数来实现。由于损失函数是二次的，因此可以通过解析方法直接求解（比梯度下降更方便）。具体来说，岭回归的参数可以通过以下公式计算得到：
   $$\theta = (X^TX+\lambda I)^{-1}X^Ty$$
3. 有现成的库函数
   
---

## 遗传算法  启发式算法/优化问题
**规划求解类**
1. 作用：规划求解是研究约束条件下目标函数的极值问题的数学理论和方法  
2. 输入：目标函数，约束条件和未知数取值范围。  
输出：规划求解结果，以及规划求解方程导出。  

<font size = 6>[遗传算法实战](https://blog.csdn.net/LOVEmy134611/article/details/111639624)</font>
### 核心思想  
遗传算法模仿生物界的自然选择和遗传规律，通过种群进化逐步优化解。基本过程包括：

1. 初始化种群：生成一组随机个体作为初始种群，每个个体表示一个可能的解。
2. 适应度评估：通过目标函数计算每个个体的适应度值，用于衡量个体的优劣。适应度函数用来衡量个体的质量，即目标函数的值。适应度越高，代表更好的解，个体越有可能被选中。
3. 选择（Selection）：根据适应度值选择下一代的父母个体，适应度高的个体有更高的概率被选中。但仍有机会选择低适应度值的个体。
4. 交叉（Crossover）：通过基因交换生成新的子代个体，从父代个体中继承优良特性。
5. 变异（Mutation）：以小概率随机改变个体的某些基因，增加种群的多样性，防止陷入局部最优。
6. 迭代与终止：重复上述步骤，直到满足终止条件（如达到最大迭代次数或达到目标精度）。

---

# B题潜水艇 2411570

## 潜水艇位置预测
1. 微分方程
   
## 搜索设备和搜索方案
1. EWM（熵权法）-TOPSIS 见14周备赛
2. 蒙特卡洛模拟方法计算出现概率  

---

# 2419984  
## 潜水艇位置预测
1. 微分方程
2. 四阶Runge-Kutta方法
   
## 搜索设备
1. 熵权法
2. 蒙特卡洛模拟   

## 搜索方案
1. 离散化为网格
2. 蒙特卡罗模拟方法计算出现概率，贝叶斯检测
3. 蚁群算法

---

# 2425792  
## 潜水艇位置预测
1. 微分方程
2. 流体动力学方程
3. 卡尔曼滤波 

## 搜索设备
1. 主成分分析（PCA）

## 搜索方案
1. 预测估计协方差矩阵
2. 多元正态分布的概率密度函数

## 外推
1. Voronoi图

---

## 卡尔曼滤波  涉及仪器检测用于减小误差
**作用**：降低仪器测量噪声对结果的影响，是一种后验修正方法。

卡尔曼滤波基于以下几个假设：
- **线性系统**：系统的状态转移方程和观测方程是线性的。
- **高斯噪声**：过程噪声和测量噪声均假设是高斯分布（零均值、已知方差）。
- **最优估计**：卡尔曼滤波通过递归的预测与更新步骤，以最小化估计误差的方差，实现对系统状态的最优估计。
假设系统的状态在时刻 \(k\) 为 \(x_k\)，它由如下状态方程和观测方程描述：

### 状态方程：
$$x_k = A x_{k-1} + B u_k + w_k$$
其中：
- $x_k$ 是时刻 $k$ 的系统状态向量。
- $A$ 是状态转移矩阵，描述系统如何从时刻 $k-1$ 转移到时刻 $k$。
- $B$ 是控制输入矩阵, $u_k$ 是控制输入。
- $w_k$ 是过程噪声，通常假设它是零均值、高斯分布，协方差为 $Q$。

### 观测方程
$$z_k = H x_k + v_k$$
其中：
- $z_k$ 是时刻 $k$ 的观测值。
- $H$ 是观测矩阵，描述如何将系统状态映射到观测空间。
- $v_k$ 是测量噪声，通常假设它是零均值、高斯分布，协方差为 $R$。
- 
### 更新步骤（Update Step）

根据新的观测数据 $z_k$ 更新状态估计：
- **创新（残差）**：
$$y_k = z_k - H \hat{x}_{k|k-1}$$ 其中 $y_k$ 是创新，也叫观测残差，表示实际测量值与预测测量值之间的差异。

- **卡尔曼增益**：
$$K_k = P_{k|k-1} H^T (H P_{k|k-1} H^T + R)^{-1}$$ 卡尔曼增益 $K_k$ 决定了状态估计的更新幅度。它的作用是将预测结果与实际测量值进行加权融合，权重由预测的不确定性和观测噪声决定。

- **状态更新**：
$$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k y_k$$ 通过创新（残差）对预测的状态进行更新，从而得到当前时刻的最优估计。

- **协方差更新**：
$$P_{k|k} = (I - K_k H) P_{k|k-1}$$ 更新状态协方差，反映更新后的不确定性。
