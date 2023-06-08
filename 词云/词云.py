from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import nltk
from nltk.corpus import stopwords

# 下载中文停用词列表
nltk.download('stopwords')
stopwords = stopwords.words('chinese')

# 加载停用词列表
stopwords = []
with open(
        "C:\\Users\\25830\\OneDrive - "
        "oganneson\\桌面\\学习\\python学习\\python_learning\\词云\\stopword.txt", "r",
        encoding="utf-8") as f:
    stopwords = f.read().splitlines()

# 打开你的.txt文件
with open(
        "C:\\Users\\25830\\OneDrive - oganneson\\桌面\\学习\\python学习\\python_learning\\词云\\21地信交流群.txt",
        'r', encoding='utf-8') as f:
    text = f.read()

# 使用 jieba 进行中文分词，并过滤停用词
seg_list = jieba.cut(text, cut_all=False)  # 精确模式
seg_list = [word for word in seg_list if word not in stopwords]  # 过滤停用词
seg_text = ' '.join(seg_list)

# 创建 WordCloud 对象
wc = WordCloud(font_path='simhei.ttf',  # 设置字体为 simhei
               background_color='white',  # 设置背景颜色
               max_words=200,  # 设置最大显示的词数
               max_font_size=240,  # 设置字体最大值
               random_state=12,  # 设置有多少种随机生成状态，即有多少种配色方案
               width=1000,  # 设置图片的宽度
               height=800,  # 设置图片的高度
               margin=2,  # 设置词与词之间的间距
               collocations=False  # 禁止词云生成相同词的组合词
               )

# 生成词云
wc.generate(seg_text)

# 展示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
