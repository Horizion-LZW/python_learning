# 文件路径
fn = "C:\\Users\\25830\\OneDrive - oganneson\\桌面\\学习\\python学习\\python_learning\\文件读写\\I have a dream.txt"

with open(fn, "r", encoding="utf-8") as f:
    text = f.read()

# 将文本转化为小写（假设我们不区分大小写）
text = text.lower()

# 移除所有标点符号
for punct in '.,"':
    text = text.replace(punct, '')

# 使用split分割单词，默认的空白符包括空格，换行符\n，制表符\t等
words = text.split()

# 统计词频
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1 # 如果字典中没有word，返回0

items = list(counts.items()) # 将字典转化为列表
items.sort(key=lambda x: x[1], reverse=True)# 按照词频从大到小排序
for i in range(10):# 打印这10个词及其出现次数
    word, count = items[i]
    print(f"{word}出现了{count}次")  # f-string是格式化字符串的一种方法，可以在字符串前加上f，然后在字符串中使用大括号{}来引用变量


