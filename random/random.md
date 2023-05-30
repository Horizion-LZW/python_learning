# random库
## 1. random库的概述
常用的函数
- random()：生成一个[0.0, 1.0)之间的随机小数
- randint(a, b)：生成一个[a, b]之间的整数
- getrandbits(k)：生成一个k比特长的随机整数
- uniform(a, b)：生成一个[a, b]之间的随机小数
- choice(seq)：从序列seq中随机选择一个元素
- shuffle(seq)：将序列seq中的元素随机排列，返回打乱后的序列
- sample(seq, n)：从序列seq中随机选择n个元素，返回选中的元素列表
- random.seed(a=None, version=2)：改变随机数生成器的种子seed，如果不设置seed，则使用系统当前时间
- random.getstate()：返回随机数生成器的内部状态
- random.setstate(state)：恢复随机数生成器的内部状态
- random.getrandbits(k)：生成一个k比特长的随机整数

seed()函数
- 作用：指定随机数生成时所用算法开始的整数值，如果使用相同的seed()值，则每次生成的随机数都相同
- 语法：random.seed(a=None, version=2)
- 参数：a：可以是任何数据类型，如果是整数，则直接使用，如果是其它类型，则使用其hash值
- 返回值：无
- 说明：如果不设置seed()值，则使用系统当前时间，定义为从1970年1月1日0时0分0秒到现在所经历的秒数

randint()函数
- 作用：生成一个[a, b]之间的整数
- 语法：random.randint(a, b)
- 参数：a：下限；b：上限
- 返回值：[a, b]之间的整数
- 说明：a、b可以是负数，但a必须小于等于b

getrandbits()函数
- 作用：生成一个k比特长的随机整数
- 语法：random.getrandbits(k)
- 参数：k：比特位数
- 返回值：k比特长的随机整数
- 说明：k必须大于0

uniform()函数
- 作用：生成一个[a, b]之间的随机小数
- 语法：random.uniform(a, b)
- 参数：a：下限；b：上限
- 返回值：[a, b]之间的随机小数
- 说明：a、b可以是负数，但a必须小于等于b

choice()函数
- 作用：从序列seq中随机选择一个元素
- 语法：random.choice(seq)
- 参数：seq：序列
- 返回值：序列seq中的一个元素
- 说明：seq必须是一个序列，可以是list、tuple、字符串等 如果seq为空，则抛出IndexError异常,如果seq为字符串，则返回一个字符,如果seq为tuple，则返回一个元组,
    如果seq为range，则返回一个整数,如果seq为list，则返回一个元素,如果seq为dict，则返回一个键,如果seq为set，则返回一个元素
  

# time库

## time.time()函数
- 作用：获取当前时间戳
- 语法：time.time()
- 参数：无
- 返回值：当前时间戳，浮点数形式，单位为秒
- 说明：时间戳是指从1970年1月1日0时0分0秒到现在所经历的秒数

## ctime()函数
- 作用：将时间戳转换为字符串
- 语法：time.ctime(seconds)
- 参数：seconds：时间戳
- 返回值：时间戳对应的字符串
- 说明：如果不传递参数，则默认使用time.time()函数的返回值
- 