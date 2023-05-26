#设置图形和坐标轴的属性
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2,100)
fig, ax = plt.subplots(figsize=(5,2.7),layout='constrained',dpi=300)
ax.plot(x,x,label='linear')#在同一幅图中画出两条曲线
ax.plot(x,x**2,label='quadratic')
ax.plot(x,x**3,label='cubic')
#ax.set(xlim=[0, 8], xticks=np.arange(1,8),
       #ylim=[0, 8], yticks=np.arange(1, 8))#设置x轴和y轴的范围和刻度
ax.set_xlabel('x label')#设置x轴标签
ax.set_ylabel('y label')#设置y轴标签
ax.set_title("Simple Plot")#设置图的标题
ax.legend()#显示图例
plt.show()#显示图像


