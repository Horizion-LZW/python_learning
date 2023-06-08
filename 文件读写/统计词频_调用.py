import collections

# 文件路径
fn = "C:\\Users\\25830\\OneDrive - oganneson\\桌面\\学习\\python学习\\python_learning\\文件读写\\I have a dream.txt"
with open(fn, "r", encoding="utf-8") as f:
    text = f.read()

# 将文本转化为小写（假设我们不区分大小写）
text = text.lower()

# 使用split分割单词，默认的空白符包括空格，换行符\n，制表符\t等
words = text.split()

# 使用collections的Counter类统计词频
word_counts = collections.Counter(words)

# 找到出现次数最多的10个词，返回一个列表，列表中的每个元素为一个元组，元组的第一个元素为单词，第二个元素为该单词的出现次数
most_common_10 = word_counts.most_common(10)

# 打印这10个词及其出现次数
for word, count in most_common_10:
    print(f'单词 "{word}" 出现了 {count} 次')
