# 第三次交流
## 一些绘图模板
1. 直方图组（含正态曲线拟合）
```python
import json
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def convert_time(timestamp, time_zone = 8):
    '''
    时间转换
    '''
    # 转换为 UTC 时间
    utc_time = dt.datetime.fromtimestamp(timestamp, tz = dt.timezone.utc)
    # 转换为东八区时间
    converted_time = utc_time.astimezone(dt.timezone(dt.timedelta(hours = time_zone)))
    return converted_time

file = "eat-data.json"

with open(file, 'r', encoding='utf-8') as f:
    data = json.load(f)
    breakfasts, lunchs, dinners = [], [], []
    for i in data["entities"]:
        time = convert_time(i["orderTime"]).hour
        if (time >= 6 and time <= 9):
            fee = -i["amount"]
            if fee <= 15:
                breakfasts.append(fee)
        elif (time >= 10 and time <= 14):
            fee = -i["amount"]
            if fee <= 50:
                lunchs.append(fee)
        elif (time >= 15 and time <= 20):
            fee = -i["amount"]
            if fee <= 50:
                dinners.append(fee)
    print(len(breakfasts), len(lunchs), len(dinners))

bpj = np.mean(breakfasts)
bsigma = np.std(breakfasts)
lpj = np.mean(lunchs)
lsigma = np.std(lunchs)
dpj = np.mean(dinners)
dsigma = np.std(dinners)


dx = 0.1
bins1 = np.arange(0, 15, dx)
bins2 = np.arange(0, 50, dx)
plt.rcParams["font.sans-serif"] = ['kaiti']     #为了显示中文才加上这一行
fig, ax = plt.subplot_mosaic('bld', layout='constrained', figsize = (9, 3))
fig.suptitle('我的2024年度食堂消费清单', fontsize = 14, fontweight = 'bold')
#如果输入的是[['b'], ['l'], ['d']]则为纵向排布
#figsize设置为宽度9，高度3


pdf1 = 1 / (np.sqrt(2 * np.pi)) / bsigma * np.exp(-(bins1 - bpj)**2 / 2 / (bsigma**2))
ax['b'].hist(breakfasts, bins=bins1, density=True, histtype='step')

# scale and plot the expected pdf:
ax['b'].plot(bins1, pdf1 * dx)
ax['b'].set_ylabel('次数/组距')
ax['b'].set_xlabel('金额（元）')
ax['b'].set_title('早餐', fontsize = 10)


pdf2 = 1 / (np.sqrt(2 * np.pi)) / lsigma * np.exp(-(bins2 - lpj)**2 / 2 / (lsigma**2))
ax['l'].hist(lunchs, bins=bins2, density=True, histtype='step', label='午餐')
ax['l'].plot(bins2, pdf2 * dx)
ax['l'].set_ylabel('次数/组距')
ax['l'].set_xlabel('金额（元）')
ax['l'].set_title('午餐', fontsize = 10)


pdf3 = 1 / (np.sqrt(2 * np.pi)) / dsigma * np.exp(-(bins2 - dpj)**2 / 2 / (dsigma**2))
ax['d'].hist(dinners, bins=bins2, density=True, histtype='step', label='晚餐')
ax['d'].plot(bins2, pdf3 * dx)
ax['d'].set_ylabel('次数/组距')
ax['d'].set_xlabel('金额（元）')
ax['d'].set_title('晚餐', fontsize = 10)

plt.show()
```

2. 分组柱状图（带标签）
```python
# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt
import numpy as np

species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

plt.show()
```

3. 3D地形图
```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Load and format data
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']           #z是一个二维数组，对应每一个平面点的具体高度值
nrows, ncols = z.shape         #获取z的行数和列数
x = np.linspace(dem['xmin'], dem['xmax'], ncols)  #构建x的线性空间
y = np.linspace(dem['ymin'], dem['ymax'], nrows)  #构建y的线性空间
x, y = np.meshgrid(x, y)       #根据x和y的线性空间创建网格。

region = np.s_[5:50, 5:50]     #划定特定区域
x, y, z = x[region], y[region], z[region]    #截取特定区域内的数据

# Set up plot
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)      #方位角设置为270度（从y轴负方向看），高度角设置为45度。
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
#vert_exag参数用于垂直夸张，增强地形的立体感
#blend_mode设置为'soft'时表示颜色柔和过渡，设置为'overlay'时表示增强颜色对比度

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
```
### 调色
- cm.gist_earth是Matplotlib提供的一种预定义的颜色映射，它模拟了地球的自然色调，通常用于表示地形、海洋深度或其他需要地球色调渐变的数据。
- cm.terrain 是一种预定义的颜色映射（colormap），它通常被设计用来表示地形数据。这种配色方案的特点是使用了一系列从绿色到棕色再到白色的颜色渐变，这些颜色能够很好地反映出地形的不同高度和特征。
- cm.viridis：一种基于视觉感知优化的颜色映射，适用于大多数科学数据可视化。
- cm.inferno、cm.magma、cm.plasma：这些颜色映射与viridis类似，但具有不同的色调和亮度分布。
- cm.coolwarm、cm.bwr（blue-white-red）、cm.RdBu（red-blue）等：这些颜色映射适用于表示有正负之分的数据，因为它们包含了从冷色调到暖色调的渐变。
- cm.gray或cm.bone：用于表示不需要强调颜色差异的数据，或者当数据的颜色编码不是主要焦点时。
- 也可以自定义：
```python
from matplotlib.colors import LinearSegmentedColormap

# 定义一个颜色列表
colors = ["blue", "cyan", "green", "yellow", "red"]

# 创建一个自定义颜色映射
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
```

4. 二维直方图
```python
import matplotlib.pyplot as plt
import numpy as np

import data_origin as d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = d.lunchs
y = d.dinners
hist, xedges, yedges = np.histogram2d(x, y, bins=20, range=[[0, 20], [0, 20]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
# 通过 + 0.25 将这些边界值稍微移动一下，以便将柱子的中心放在每个区间的中心位置。
# 这里的 0.25 是基于假设每个区间宽度为1（由于数据被缩放到0-20范围，并且分成了20个区间，所以每个区间大约1个单位宽），
# 并且我们想要柱子中心位于区间中点，所以加了区间宽度的一半（即0.5的一半，为0.25）。(区间宽度0.5在下面设置了)

xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
# 0.5 * ...：将上述创建的全1数组的每个元素都乘以0.5，意味着我们想要每个柱子的宽度（dx）和高度（dy）都是0.5个单位。

dz = hist.ravel()
# 这个函数会将二维数组hist展平为一维数组。这是为了与xpos、ypos（它们也是一维数组）以及后续绘图函数ax.bar3d的参数要求相匹配。

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
# zsort='average'参数用于在绘制时根据z值的平均值来排序柱子，以避免遮挡问题。

plt.show()
```

5. 等高线地形图
```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

# Load and format data
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']           #z是一个二维数组，对应每一个平面点的具体高度值
nrows, ncols = z.shape         #获取z的行数和列数
x = np.linspace(dem['xmin'], dem['xmax'], ncols)  #构建x的线性空间
y = np.linspace(dem['ymin'], dem['ymax'], nrows)  #构建y的线性空间
x, y = np.meshgrid(x, y)       #根据x和y的线性空间创建网格。

region = np.s_[5:50, 5:50]     #划定特定区域
x, y, z = x[region], y[region], z[region]    #截取特定区域内的数据

# Set up plot
fig, ax = plt.subplots()

# 使用指定的颜色映射来绘制等高线填充图
cmap = cm.terrain  # 您可以更改此颜色映射为您喜欢的任何颜色映射
surf = ax.contourf(x, y, z, cmap=cmap, antialiased=False)
 
# 添加颜色条
fig.colorbar(surf, ax=ax, label='Elevation (m)')

plt.show()
```

6. 雷达图组图
```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections import register_projection
from matplotlib.projections.polar import PolarAxes
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D


def radar_factory(num_vars, frame='circle'):
    """
    Create a radar chart with `num_vars` Axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding Axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):

        def transform_path_non_affine(self, path):
            # Paths with non-unit interpolation steps correspond to gridlines,
            # in which case we force interpolation (to defeat PolarTransform's
            # autoconversion to circular arcs).
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):

        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def example_data():
    # The following data is from the Denver Aerosol Sources and Health study.
    # See doi:10.1016/j.atmosenv.2008.12.017
    #
    # The data are pollution source profile estimates for five modeled
    # pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
    # species. The radar charts are experimented with here to see if we can
    # nicely visualize how the modeled source profiles change across four
    # scenarios:
    #  1) No gas-phase species present, just seven particulate counts on
    #     Sulfate
    #     Nitrate
    #     Elemental Carbon (EC)
    #     Organic Carbon fraction 1 (OC)
    #     Organic Carbon fraction 2 (OC2)
    #     Organic Carbon fraction 3 (OC3)
    #     Pyrolyzed Organic Carbon (OP)
    #  2)Inclusion of gas-phase specie carbon monoxide (CO)
    #  3)Inclusion of gas-phase specie ozone (O3).
    #  4)Inclusion of both gas-phase species is present...
    data = [
        ['Sulfate', 'Nitrate', 'EC', 'OC1', 'OC2', 'OC3', 'OP', 'CO', 'O3'],
        ('Basecase', [
            [0.88, 0.01, 0.03, 0.03, 0.00, 0.06, 0.01, 0.00, 0.00],
            [0.07, 0.95, 0.04, 0.05, 0.00, 0.02, 0.01, 0.00, 0.00],
            [0.01, 0.02, 0.85, 0.19, 0.05, 0.10, 0.00, 0.00, 0.00],
            [0.02, 0.01, 0.07, 0.01, 0.21, 0.12, 0.98, 0.00, 0.00],
            [0.01, 0.01, 0.02, 0.71, 0.74, 0.70, 0.00, 0.00, 0.00]]),
        ('With CO', [
            [0.88, 0.02, 0.02, 0.02, 0.00, 0.05, 0.00, 0.05, 0.00],
            [0.08, 0.94, 0.04, 0.02, 0.00, 0.01, 0.12, 0.04, 0.00],
            [0.01, 0.01, 0.79, 0.10, 0.00, 0.05, 0.00, 0.31, 0.00],
            [0.00, 0.02, 0.03, 0.38, 0.31, 0.31, 0.00, 0.59, 0.00],
            [0.02, 0.02, 0.11, 0.47, 0.69, 0.58, 0.88, 0.00, 0.00]]),
        ('With O3', [
            [0.89, 0.01, 0.07, 0.00, 0.00, 0.05, 0.00, 0.00, 0.03],
            [0.07, 0.95, 0.05, 0.04, 0.00, 0.02, 0.12, 0.00, 0.00],
            [0.01, 0.02, 0.86, 0.27, 0.16, 0.19, 0.00, 0.00, 0.00],
            [0.01, 0.03, 0.00, 0.32, 0.29, 0.27, 0.00, 0.00, 0.95],
            [0.02, 0.00, 0.03, 0.37, 0.56, 0.47, 0.87, 0.00, 0.00]]),
        ('CO & O3', [
            [0.87, 0.01, 0.08, 0.00, 0.00, 0.04, 0.00, 0.00, 0.01],
            [0.09, 0.95, 0.02, 0.03, 0.00, 0.01, 0.13, 0.06, 0.00],
            [0.01, 0.02, 0.71, 0.24, 0.13, 0.16, 0.00, 0.50, 0.00],
            [0.01, 0.03, 0.00, 0.28, 0.24, 0.23, 0.00, 0.44, 0.88],
            [0.02, 0.00, 0.18, 0.45, 0.64, 0.55, 0.86, 0.00, 0.16]])
    ]
    return data


if __name__ == '__main__':
    N = 9
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, axs = plt.subplots(figsize=(9, 9), nrows=2, ncols=2,
                            subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b', 'r', 'g', 'm', 'y']
    # Plot the four cases from the example data on separate Axes
    for ax, (title, case_data) in zip(axs.flat, data):
        ax.set_rgrids([0.2, 0.4, 0.6, 0.8])
        ax.set_title(title, weight='bold', size='medium', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25, label='_nolegend_')
        ax.set_varlabels(spoke_labels)

    # add legend relative to top-left plot
    labels = ('Factor 1', 'Factor 2', 'Factor 3', 'Factor 4', 'Factor 5')
    legend = axs[0, 0].legend(labels, loc=(0.9, .95),
                              labelspacing=0.1, fontsize='small')

    fig.text(0.5, 0.965, '5-Factor Solution Profiles Across Four Scenarios',
             horizontalalignment='center', color='black', weight='bold',
             size='large')

    plt.show()
```

7. 箱型图
```python
import matplotlib.pyplot as plt
import numpy as np

import data_origin as d

np.random.seed(19680801)
fruit_weights = [
    d.breakfasts,
    d.lunchs,
    d.dinners,
]
labels = ['breakfasts', 'lunchs', 'dinners']
colors = ['pink', 'orange', 'gold']

fig, ax = plt.subplots()
ax.set_ylabel('fruit weight (g)')

bplot = ax.boxplot(fruit_weights,
                   patch_artist=True,  # fill with color
                   tick_labels=labels)  # will be used to label x-ticks

# fill with colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()
```
PS：箱型图上的小圆圈表示异常数据