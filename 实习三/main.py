#热力图

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib

vegetabnles =["cucumber","tomato","lettuce","asparagus","potato","wheat","barley"]
farmers = ["Farmer Joe","Upland Bros.","Smith Gardening","Agrifun","Organiculture","BioGoods Ltd.","Cornylee Corp."]
harvest = np.array([[0.8,0.3,0.4,0.9,0.2,0.1,0.7],
                    [0.2,0.8,0.5,0.7,0.1,0.6,0.2],
                    [0.3,0.5,0.9,0.8,0.3,0.8,0.6],
                    [0.6,0.6,0.7,0.9,0.6,0.7,0.4],
                    [0.6,0.7,0.6,0.4,0.8,0.7,0.6],
                    [0.3,0.4,0.7,0.2,0.8,0.8,0.7],
                    [0.4,0.3,0.8,0.5,0.7,0.6,0.8]])

fig, ax = plt.subplots()#创建一个图形和一组子图
matplotlib.rcParams['figure.dpi'] = 600  # 设置图形dpi
im = ax.imshow(harvest)#绘制热力图

#show all ticks and label them with the respective list entries 展示所有的刻度并且用相应的列表条目标记它们
ax.set_xticks(np.arange(len(farmers)),labels=farmers)#设置x轴的刻度和标签
ax.set_yticks(np.arange(len(vegetabnles)),labels=vegetabnles)#设置y轴的刻度和标签

# rotate the tick labels and set their alignment. 旋转刻度标签并设置其对齐方式
plt.setp(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode="anchor")#设置x轴刻度标签的旋转角度，对齐方式，旋转模式

#loop over data dimensions and create text annotations.循环数据维度并创建文本注释
for i in range(len(vegetabnles)):
    for j in range(len(farmers)):
        text = ax.text(j,i,harvest[i,j],ha="center",va="center",color="w")#在图中添加文本注释

ax.set_title("Harvest of local farmers (in tons/year)")#设置图的标题
fig.tight_layout()#调整子图参数，使之填充整个图像区域
plt.show()#显示图像

