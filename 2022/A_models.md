# 功率曲线
有氧功率+无氧功率，设定为输出功率小于等于有氧功率持续时间可以看作无穷，输出功率大于有氧功率时持续时间随功率增大而减少
要点：  
1. 量化输出功率和维持时间的关系
2. 考虑疲劳与超限的影响
3. 考虑总能量的影响

## 无氧能量池基本方程
选手的无氧能量池为W，初始无氧能量为AWC，额定有氧功率为CP，当前输出功率为P，恢复疲劳阶段实际输出功率为 $P_{adj}$，满足 
$$
\begin{equation}
\frac{dW}{dt}=
\begin{cases}
    -(P-CP) &\text{if } P > CP \\
    -(P_{adj}-CP) &\text{if } P < CP
    \end{cases}    
\end{equation}
$$
其中$P_{adj}$与P的关系满足，其与CP的差值用于恢复无氧能量池
$$
\begin{equation}
P_{adj} = P-（aP+b）e^{-\lambda t}
\end{equation}$$
$\lambda$与当前无氧能量池的大小相关。



## 输出功率基本方程
当前时刻的无氧能量池数值为 $W(t)$，当前时刻的最大输出功率 $P_max(t)$与$W(t)$的关系可以表示为
$$
\begin{equation}
P_{max}(t)=a_1W^2(t)+a_2W(t)+CP
\end{equation}$$
实际输出功率并不会等于$P_{max}$，而是处于$P_{max}$与CP之间的定值P，  
求解公式（1）和公式（3）确定的微分方程，解得使$P_{max}(T)<P$的时刻T即为能输出功率P的维持时间。 
不同类型选手的影响参数：AWC，CP   

## 超限功率带来的影响
方程（3）给出了在无氧能量池为$W(t)$的最大输出功率$P_{max}$，而当运动员以超过$P_{max}$的功率运动时，会对之后的输出功率产生影响，需要更长的时间进行恢复。使用 
 $W_{ex}$代表超出功率曲线范围的无氧能量消耗，其会降低无氧最大功率和无氧能量池恢复速度。修改方程（3）
$$
\begin{equation}
P_{max}(t)=（1-\gamma W_{ex}）（a_1W^2(t)+a_2W(t)）+CP
\end{equation}$$
同时修改无氧能量池的恢复速度也乘以系数 $（1-\gamma W_{ex}）$
暂未考虑超限是否可以恢复的问题，**有待细化**

---

# 赛道模型
赛道定义为 $l(s,\theta,\mu,\rho,\vec{v_w})$,表示为一段情形相似的赛道$l$，长度为s，上坡时坡度$\theta$为正值，摩擦系数为$\mu$，曲率半径为$\rho$，$\vec{v_w}$表示沿当前赛道的风速和方向。

---

# 动力学模型建立
## 受力分析
### 1.坡度与摩擦系数带来的阻力或动力
令坡度阻力和摩擦阻力为 $f_{\theta}$， $f_{\theta}<0$时为阻力， $f_{\theta}>0$时为动力，方程为：
$$
\begin{equation}
f_{\theta}=-mgsin\theta-\sqrt{(\mu mgcos\theta)^2-(\frac{mv^2}{R})^2}
\end{equation}$$
其中$\frac{mv^2}{R}$为保持圆周运动的法向摩擦力，将在3中讨论。

### 2.风速带来的阻力或动力
令$\vec{v_r} = \vec{v}-\vec{v_w}$，风阻$f_{air}$，正负定义同上，方程为：
$$\begin{equation}
f_{air}=\frac{1}{2}\rho_0C_dA |\vec{v_r}|^2\cdot\frac{\vec{v_r} \cdot \vec{v}}{|\vec{v_r}||\vec{v}|}
\end{equation}$$
* $\rho_0$是空气密度。
* $C_d$是空气阻力系数，通常取决于骑行者的姿势、衣物、车架设计等因素。
* $A$是正面投影面积。

### 3.转弯曲率对速度的限制
转弯曲率与赛道坡度和曲率半径关系为：
$$\begin{equation}
R = \rho \sqrt{1+tan^2\theta}
\end{equation}$$

压弯水平不同，暂不考虑。认为静摩擦力的分量完全提供法向向心力。
$$\begin{equation}
\frac{mv^2}{R} \leq \mu mgcos\theta 
\end{equation}$$
解得不同赛段最大速度的限制：
$$\begin{equation}
v_{max} \leq \sqrt{\mu gRcos\theta}
\end{equation}$$

---

## 建立动力学模型
$$\begin{equation}
\alpha P+f_{\theta} \cdot v+f_{air} \cdot v = \frac{dE_k}{dt} = mv\frac{dv}{dt}
\end{equation}$$
$$\begin{equation}
\frac{dv}{dt}=\alpha \frac{P}{mv}-gsin\theta-\sqrt{(\mu gcos\theta)^2-\frac{v^4}{R^2}}+\frac{1}{2m}\rho_0C_dA |\vec{v_r}|^2\cdot\frac{\vec{v_r} \cdot \vec{v}}{|\vec{v_r}||\vec{v}|}
\end{equation}$$
其中$\alpha$为自行车的功率传动效率。
有路程的关系：
$$\begin{equation}
    s_i = \int_{t_i}^{t_{i+1}}v(t)dt
\end{equation}
$$
确定P（t）或者P（s）(待求解的策略)，求解微分方程并用总路程即可求得时间。  
方案规模量太大，使用启发式算法。
