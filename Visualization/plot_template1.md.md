# 第二次交流
## 数据交互与可视化
### 1. 读取CSV格式文本文件
```python
file = "data/weather.csv" #此处双引号内填入相对路径

with open(file) as f:
    reader = f.read()
```
若要读取以后转化成相应的格式（CSV转化成列表，JSON转化成字典）
```python
import json
file = "data/earthquake.json"

with open(file) as f:
    reader = json.load()   #此处是转化成相应格式

with open("new_json.json", 'w') as g :    #'w'表示写入
    json.dump(reader, g, indent=4)
    #此处是写进一个新的json文件里面去，indent=4是一个参数，与格式有关
```
```python
import csv
file = "data/weather.csv" #此处双引号内填入相对路径

with open(file) as f:
    reader = csv.reader(f)     #注意：此时reader并不是一个列表
    line_list = next(reader)   #输出结果为csv文件的第一行构成的一个列表
    line_list2 = next(reader)  #输出结果为csv文件的第二行构成的一个列表
```
在上述基础上，若要取出csv文件中某特定类别的数值
```python
import csv
file = "data/weather.csv" #此处双引号内填入相对路径

with open(file) as f:
    reader = csv.reader(f)     #注意：此时reader并不是一个列表
    line_list = next(reader)   #输出结果为csv文件的第一行构成的一个列表

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
```
### 2. 开始画图
加载出直角坐标系
```python
import matplotlib.pyplot as plt

plt.subplots(3, 2)
#第一个参数表示有多少行，第二个参数表示有多少列

plt.show()
```

![实际效果]("my_pictures\zuobiaoxi.png")

导入数据并绘制折线图
```python
import matplotlib.pyplot as plt
import data_origin

fig, ax = plt.subplots()

ax.plot(data_origin.highs)

plt.show()
```
导入多行数据并修改折线颜色
```python
import matplotlib.pyplot as plt
import data_origin

fig, ax = plt.subplots()

ax.plot(data_origin.lunchs, c = "blue")
ax.plot(data_origin.dinners, c = "red")

plt.show()
```
![折线图效果]('my_pictures\zhexiantu.pdf')

导入横轴数据，并修改横轴显示
```python
import matplotlib.pyplot as plt
import data_origin

fig, ax = plt.subplots()

ax.plot(data_origin.dates, data_origin.lunchs, c = "blue")
ax.plot(data_origin.dates, data_origin.dinners, c = "red")

ax.axes.xaxis.set_ticks([0, 5, 10, 15, 20, 25, 29])    #间隔显示
fig.autofmt_xdate()   #设置横轴倾斜显示

plt.show()
```
![横轴效果]('my_pictures\zhexiantu(pro).pdf')

绘制散点
```python
import matplotlib.pyplot as plt
import data_origin

fig, ax = plt.subplots()

ax.plot(data_origin.dates, data_origin.lunchs, c = "blue")
ax.plot(data_origin.dates, data_origin.dinners, c = "red")

#绘制散点
ax.scatter(data_origin.dates, data_origin.lunchs, c = "blue")
ax.scatter(data_origin.dates, data_origin.dinners, c = "red")

ax.axes.xaxis.set_ticks([0, 5, 10, 15, 20, 25, 29])    #间隔显示
fig.autofmt_xdate()   #设置横轴倾斜显示

plt.show()
```
填充颜色
```python
import matplotlib.pyplot as plt
import data_origin

fig, ax = plt.subplots()

ax.plot(data_origin.dates, data_origin.lunchs, c = "blue")
ax.plot(data_origin.dates, data_origin.dinners, c = "red")

#在两折线之间填充颜色
ax.fill_between(data_origin.dates, data_origin.lunchs, data_origin.dinners, facecolor='yellow', alpha=0.1)
#填充颜色为黄色，透明度为10%

ax.axes.xaxis.set_ticks([0, 5, 10, 15, 20, 25, 29])    #间隔显示
fig.autofmt_xdate()   #设置横轴倾斜显示

plt.show()
```
更多设置
```python
import matplotlib.pyplot as plt
import data_origin

plt.style.use('seaborn-v0_8-white')   #设置背景
fig, ax = plt.subplots()

ax.plot(data_origin.dates, data_origin.lunchs, c = "blue")
ax.plot(data_origin.dates, data_origin.dinners, c = "red")
ax.fill_between(data_origin.dates, data_origin.lunchs, data_origin.dinners, color = "green", alpha = 0.2)

#方式一
ax.axes.xaxis.set_ticks([0, 5, 10, 15, 20, 25, 29])    #间隔显示

#方式二
#ax.axes.yaxis.set_ticks(range(0, 5, 29))

#方式三
#plt.xticks(['9.1', '9.6', '9.11', '9.16', '9.21', '9.26', '9.30'])

fig.autofmt_xdate()   #设置横轴倾斜显示

plt.rcParams["font.sans-serif"] = ['Microsoft YaHei']     #为了显示中文才加上这一行
ax.set_title('我的9月午晚餐支出', fontsize = 18)
ax.set_xlabel('日期', fontsize = 14)
ax.set_ylabel('金额（元）', fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
```
画饼
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

tab20c = plt.color_sequences["tab20c"]
outer_colors = [tab20c[i] for i in [4, 0, 8, 12]]
# inner_colors = [tab20c[i] for i in [1, 2, 5, 6, 9, 10]]

data = [375, 75, 250, 200]
ingredients = ["flour", "sugar", "butter", "berry"]

wedges, texts = ax.pie(data, labels=["37.5%", "7.5%", "25%", "20%"], textprops=dict(color="black"), 
                radius=0.8, colors=outer_colors,
                wedgeprops=dict(width=size, edgecolor='w'))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
热力图
```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl


vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])


fig, ax = plt.subplots()
im = ax.imshow(harvest, cmap = 'RdBu')

# Show all ticks and label them with the respective list entries
ax.set_xticks(range(len(farmers)), labels=farmers,
              rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(range(len(vegetables)), labels=vegetables)
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("harvest [t/year]", rotation=-90, va="bottom")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="#EBF10D")

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()
```
3D折线图
```python
import matplotlib.pyplot as plt
import numpy as np

import data_origin

ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
z = data_origin.breakfasts
x = data_origin.lunchs
y = data_origin.dinners

ax.plot(x, y, z, label='parametric curve', c = "red")
ax.legend()

plt.show()
```
3D散点图
```python
import matplotlib.pyplot as plt
import numpy as np

import data_origin

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = data_origin.breakfasts
    ys = data_origin.lunchs
    zs = data_origin.dinners
    ax.scatter(xs, ys, zs, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
```
## 一些有用的网址
[配色网站](https://mycolor.space/)
[图片素材库](https://www.freepik.com/)
[matplotlib库示例图及其代码](https://matplotlib.org/stable/gallery/index.html)
[seaborn库示例图及其代码](https://seaborn.pydata.org/)
[SPSSPRO：检验绘图效果](https://www.spsspro.com/)