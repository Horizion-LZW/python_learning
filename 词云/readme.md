```python
# 导入所需要的库
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

# 打开你的.txt文件
with open('D:\\yaoganguochengshuju\\2.8\\实习报告.txt', 'r',
          encoding='utf-8') as f:
    text = f.read()

# 使用 jieba 进行中文分词
seg_list = jieba.cut(text, cut_all=False)  # 精确模式
seg_text = ' '.join(seg_list)

# 创建 WordCloud 对象
wc = WordCloud(font_path='simhei.ttf',  # 设置字体为 simhei
               background_color='white',  # 设置背景颜色
               max_words=1000,  # 设置最大显示的词数
               max_font_size=500,  # 设置字体最大值
               random_state=12,  # 设置有多少种随机生成状态，即有多少种配色方案
               width=1920,  # 设置图片的宽度
               height=1080  # 设置图片的高度
               )

# 生成词云
wc.generate(seg_text)

# 展示词云
plt.imshow(wc)
plt.axis('off')
plt.show()

```
![img.png](img.png)