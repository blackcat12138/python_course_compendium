'''
    正则分组
        |  或者符号
        () 整体的一组字符 (word|word|word) 区别 [abc]
        [] 单个字母,表示一个范围 [0-9]
         +  至少要有一个字母
         .  任意字符
    量词
         ？     0,1
         *      >=0
         +      >=1
         {m}    =m
         {m,}   >=m
         {m,n}  >=m <=n
    分组：
        ()   -----> group(2)
    number
        (\w+)(\d*)  ---> group(1) group(2)
        (\w+)(\d*)  ---> \1 \2 表示引用前面的内容
    name
        (?P<名字>正则)(?P=名称)
'''
# 匹配数字0-100数字
import re

n = '100'

resul = re.match('[1-9]?\d', n)
print(resul)

# 改进版
result = re.match(r'[1-9]?\d?$|100$', n)
print(result)

# 验证输入的邮箱 163 126 qq
email = '12138@163.com'

erm = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
print(erm)

# 不是以4、7结尾的手机号码(11位)
ph = '18682369392'
rps = re.match(r'1\d{9}[0-35-689]$', ph)
print(rps)

# 匹配带区号到电话号码
phone = '010-12345678'
rph = re.match(r'(\d{3}|\d{4})-(\d{8,})$', phone)
print(rph.group())
print(rph.group(2))

# qq号码验证5~11
qq = '738516789'
rq = re.match('^[1-9][0-9]{5,}$', qq)
print(rq)

print('-----------two------------')
# search() : 只要匹配到就不往后匹配
s = 'hadd5afd3dfjt4ds'
rs = re.search('[a-z][0-9][a-z]', s)
print(rs.group())

# findall()：将全部字符串进行匹配,检索到一个继续向下找一直到结尾,全部放到列表
rss = re.findall('[a-z][0-9][a-z]', s)
print(rss)

# sub(正则,新内容,string)： 通过正则将旧内容替换成新内容（也可以替换匹配函数）
rsb = re.sub(r'\d+', '20000', 'java:201,python:234')
print(rsb)


# sub替换函数内容
def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


rsbs = re.sub(r'\d+', func, 'c++：20,shell：45')
print(rsbs)

# split() ：在字符串中搜索若遇到,或:将会进行分割,内容保存到列表中
rsp = re.split(r'[,:]', 'c++:20,shell:45')
print(rsp)

print('-----------three------------')
# 正则中的贪婪模式,若想将贪婪模式变成非贪婪模式只要加'?'
msg = 'a2aop33akia345a'
rsg = re.findall('[a-z][0-9]+[a-z]', msg)
print(rsg)

# 起名的方式匹配 : (?P<名字>正则)(?P=名称)
msga = '<html><h1>abc</h1></html>'

rngs = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msga)
print(rngs.group())

rng = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msga)
print(rng.group(1))
print(rng.group())


