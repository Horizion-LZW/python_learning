# 条形图
# axes.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
'''
`axes.bar()`是matplotlib库的一个函数，用于在给定的轴上创建条形图。让我们详细了解下每个参数的作用：
- `x`: 这是一个数组，表示条形的 x 轴坐标。这可以是数字或者是一组类别。
- `height`: 这是一个数组，与x参数长度相同，表示每个条形的高度。
- `width`: 这是一个可选参数，默认值为 0.8。它表示每个条形的宽度。
- `bottom`: 这是一个可选参数，默认值为None。它是一个数组，用于定义每个条形的 y 轴坐标。
- `align`: 这是一个可选参数，默认值为 'center'。它决定了条形的对齐方式，可选的值有 'center' 和 'edge'。如果设置为 'center'，条形将以 x 位置为中心。如果设置为 'edge'，条形将以 x 位置为左边缘。
- `data`: 这是一个可选参数，默认值为None。如果提供了这个参数，那么其他的参数可以通过字符串来从这个数据对象中选择。
- `**kwargs`: 这是一种允许你传入任意数量的关键字参数的机制。在 `axes.bar()` 函数中，这些关键字参数可以被用来指定条形图的不同属性，比如颜色、标签、边缘颜色等。
'''

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = 0.5 + np.arange(8)  # 生成0.5-8的等差数列
y = np.random.uniform(2, 7, len(x))  # 生成2-7之间的随机数，长度为x的长度 uniform均匀分布
# plot
fig, ax = plt.subplots()
ax.bar(x, y, width=1, align='center', edgecolor='white', alpha=0.8)  # alpha透明度
# align对齐方式
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))  # 设置x,y轴的范围，以及刻度
plt.show()

