#箱型图
'''
Axes.boxplot(self, x, notch=None, sym=None, vert=None, whis=None, positions=None,
            widths=None, patch_artist=None, bootstrap=None, usermedians=None, conf_intervals=None,
            meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None,
            labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None,
             manage_ticks=True, autorange=False, zorder=None)

Matplotlib库的`boxplot`方法用于创建箱形图，这是一种用于显示数据分布的图表。以下是参数的具体解释：
- `x`：需要创建箱形图的数据。
- `notch`：是否是凹口的形式展现箱线图，默认非凹口；如果为True，会有一个缺口表示中位数的置信区间。
- `sym`：指定异常点的形状，默认为+号显示。
- `vert`：是否需要将箱线图垂直摆放，默认垂直摆放。
- `whis`：指定上下须与上下四分位的距离，默认是1.5倍的四分位差。
- `positions`：箱线图的位置，默认为[0,1,2…]。
- `widths`：箱线图的宽度，默认为0.5。
- `patch_artist`：是否填充箱体的颜色；默认为False。
- `meanline`：是否用线的形式表示均值，默认用点来表示。
- `showmeans`：是否显示均值，默认不显示。
- `showcaps`：是否显示箱线图顶端和末端的两条线（即“胡须”），默认显示。
- `showbox`：是否显示箱线图的箱体，默认显示。
- `showfliers`：是否显示异常值，默认显示。
- `boxprops`：设置箱体的属性，如边框色，填充色等。
- `labels`：为箱线图添加标签，类似于图例的作用。
- `flierprops`：设置异常值的属性，如异常点的形状、大小、填充色等。
- `medianprops`：设置中位数的属性，如线的类型、粗细等。
- `meanprops`：设置均值的属性，如点的大小、颜色等。
- `capprops`：设置箱线图顶端和末端线条的属性，如颜色、粗细等。
- `whiskerprops`：设置须的属性，如颜色、粗细、线的类型等。
- `manage_ticks`: 如果为True（默认值），ticks将会被设定以在数据点周围产生空间。这会覆盖x轴和y轴上的设置。
- `autorange`：当True (默认为False)时，箱线图的范围会根据数据的范围进行调整。
- `zorder`：用于控制绘图元素的绘制顺序。具有更高zorder值的元素会被绘制在具有较低zorder值的元素之上。
以上是关于`Axes.boxplot()`函数的参数的简要说明。如果你想获取更详细的信息，建议查看[matplotlib官方文档](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)。
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')#设置绘图风格

# make data
np.random.seed(10)
D = np.random.normal((3,5,4),(1.25,1.00,1.25),(100,3))#均值，标准差，数据量

# plot
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1.5, patch_artist=True,
                # 设置箱型图的位置，宽度，是否填充
                showmeans=False, showfliers=False,  # 不显示均值，异常值
                medianprops={"color": "white", "linewidth": 0.5},  # 中位数线的属性
                boxprops={"color": "black", "edgecolor":"white",
                          "linewidth": 0.5},  # 箱体属性
                whiskerprops={"color": "C1", "linewidth": 1.5},  # 须的属性
                capprops={"color": "C1", "linewidth": 1.5},  # 顶端和末端线条的属性
                )
ax.set(xlim=[0, 8], xticks=np.arange(2, 7, 2),
       ylim=[0, 8], yticks=np.arange(1, 8))  # 设置x轴和y轴的范围和刻度
ax.set_xticklabels(["A", "B", "C"])  # 设置x轴刻度标签
ax.set_yticklabels(["1", "2", "3", "4", "5", "6", "7"])  # 设置y轴刻度标签
plt.show()

