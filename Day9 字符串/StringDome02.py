# 1.字母大小的处理
#     str.upper()：全部大写
#     str.lower(): 全部小写
#     str.swapcase()：大小写互换
#     str.capitalize()：首写字母大写,其余小写。
#     str.title()：首字母大写

a = 'hello world'

print(a.upper())  # HELLO WORLD
print(a.lower())  # hello world
print(a.swapcase())  # HELLO WORLD
print(a.capitalize())  # Hello world
print(a.title())  # Hello World

# 2.格式化字符串处理
#     str.ljust(width)：获取固定长度,左对齐,右边不够用空格补充。
#     str.rjust(width)：获取固定长度，右对齐，左边不够用空格补齐。
#     str.center(width)：获取固定长度，中间对齐，两边不够用空格补齐。
#     str.zfill(width)：获取固定长度，右对齐，左边不足用0补齐。

b = '1 2'
print(b.ljust(10))  # 1 2
print(b.rjust(10))  # 1 2
print(b.center(10))  # 1 2
print(b.zfill(10))  # 00000001 2

# 3.字符串搜索相关
#     str.find()：搜索指定字符串,没有返回-1。
#     str.index()：搜索指定字符串,若找不到则报错。
#     str.rfind()：从右边开始搜索查找。
#     str.count()：统计指定的字符串出现的次数。

s = 'hello world'
print(s.find('e'))  # 1
print(s.find('w', 1, 2))  # -1
print(s.index('w', 1, 2))  # 报错
print(s.count('o'))  # 2
print(s.rfind('w'))  # 6

# 4.字符串的替换
#     str.replace('old','new')：替换old为new。
#     str.replace('old','new',次数)：替换指定次数的old为new

x='hello world'
print(x.replace('world','python'))      # hello python
print(x.replace('l','p',2))             # heppo world
print(x.replace('l','p',4))             # heppo worpd

# 5.字符串去空格及去指定字符
#     str.strip()：去除两边空格。
#     str.lstrip()：去除左边空格。
#     str.rstrip()：去右边空格。
#     str.split()：默认按空格分隔,并返回列表。
#     str.split('指定字符')：按指定字符分割字符串为列表

y=' h e - l lo  '
print(y.strip())    # h e - l lo
print(y.lstrip())   # h e - l lo
print(y.rstrip())   # h e - l lo
print(y.split())    # ['h', 'e', '-', 'l', 'lo']
print(y.split('-')) # [' h e ', ' l lo  ']

# 6.字符串判断相关
#     str.startswith('start')：是否以start开头。
#     str.endswith('end')：是否以end结尾。
#     str.isalnum()：是否全为字母或数字。
#     str.isalpha()：是否全字母。
#     str.isdigit()：是否全为数字。
#     str.islower()：是否全为小写。
#     str.isupper()：是否全为大写。
#     str.istitle()：判断首写字母是否为大写。
#     str.isspace()：判断字符是否为空格。

# 7.补充
#     bin()：十进制数转八进制。
#     hex()：十进制数转十六进制。
#     range()：可以生成一个整数序列。
#     type()：查看数据类型。
#     len()：计算字符串长度。
#     format()：格式化字符串，类似%s，传递值能多不能少。