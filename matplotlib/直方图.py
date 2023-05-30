# 直方图
# axes.hist(x, bins, range, density, weights, cumulative, bottom, histtype, align, orientation, rwidth, log, color, label, stacked, normed, hold, data, **kwargs)
'''
`axes.hist()`
是matplotlib库的一个函数，用于在给定的轴上创建直方图。下面是每个参数的详细解释：
- `x`: 这是输入数组或者序列，表示需要计算并生成直方图的数据。
- `bins`: 这是一个可选参数，表示直方图的柱形数目。可以是一个整数或者一个序列。如果是一个序列，它定义了bin
edges，包括右边界。如果未定义，则默认值为10。
- `range`: 这是一个可选参数，表示需要计算直方图的数值范围。如果没有指定，range参数默认为(
    x.min(), x.max())。如果指定了bins为整数，range参数影响了bin的宽度。
- `density`: 这是一个可选参数，如果设置为True，则直方图将首先被标准化，然后再绘制，使得直方图下面的面积为1。
- `weights`: 这是一个可选参数，如果提供了这个参数，它必须和x参数的形状相同。这个参数可以用来为每个x值提供权重。
- `cumulative`: 这是一个可选参数，如果设置为True，那么直方图将是一个累积直方图。
- `bottom`: 这是一个可选参数，如果给出了，每个bin的底部位置就会被移到这个位置。默认为None。
- `histtype`: 这是一个可选参数，表示直方图的类型。可以是'bar', 'barstacked', 'step', 'stepfilled'。
- `align`: 这是一个可选参数，表示bin的对齐方式，可以是'left', 'mid', 'right'。
- `orientation`: 这是一个可选参数，表示直方图的方向。可以是'horizontal', 'vertical'。
- `rwidth`: 这是一个可选参数，表示bar的相对宽度。
- `log`: 这是一个可选参数，如果设置为True，那么y轴将会以对数刻度来显示。
- `color`: 这是一个可选参数，表示直方图的颜色。
- `label`: 这是一个可选参数，表示用于直方图的标签。
- `stacked`: 这是一个可选参数，如果设置为True，那么多数据系列将会被堆叠在一起。默认为False。
- `normed`: 这是一个可选参数，现已被弃用，被`density`参数取代。
- `hold`: 这是一个可选参数，现已被弃用，用于控制是否在当前轴上重绘直方图。
- `data`: 这是一个可选参数，如果提供了这个参数，那么其他的参数可以通过字符串来从这个数据对象中选择。
- ` ** kwargs`: 这是一种允许你传入任意数量的关键字参数的机制。在`axes.hist()`函数中，这些关键字参数可以被用来指定直方图的不同属性，比如颜色、标签、边缘颜色等。
'''

import matplotlib.pyplot as plt
import numpy as np
import time

plt.style.use('fast')

# make data
np.random.seed(int(time.time()))  # 以时间戳作为随机数种子
x = 4 + np.random.normal(0, 1.5, 200)  # 均值为4，标准差为1.5，200个数据

# plot
fig, ax = plt.subplots()
ax.hist(x, bins=8,linewidth=0.5, range=(0, 8), color='C0',edgecolor='C1',label='histogram')  # bins为柱形数目，range为数值范围，density为标准化，color为颜色，edgecolor为边缘颜色，label为标签
#若s设置density=True，则直方图下面的面积为1,也就是说，直方图的高度表示的是概率密度，而不是计数。
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
         ylim=(0, 56), yticks=np.linspace(0, 56, 9))  # 设置x,y轴的范围，以及刻度
ax.legend()  # 显示图例
plt.show()
