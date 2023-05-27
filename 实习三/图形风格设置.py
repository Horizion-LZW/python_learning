import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')  # 设置图形风格

# make data
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2, label='sine wave')  # 画出曲线
ax.set_title('A sine wave', fontsize=18)  # 设置标题和字体大小
ax.set_xlabel('x', fontsize=14)  # 设置x轴标签和字体大小
ax.set_ylabel('y', fontsize=14)  # 设置y轴标签和字体大小
ax.set(xlim=(0, 10), xticks=np.arange(1, 11),
       ylim=(0, 10), yticks=np.arange(1, 11))  # 设置x轴和y轴的范围和刻度
plt.show()