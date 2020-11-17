'''
    正则表达式对用户qq号码的验证
       re模块：正则处理模块
    知识点总结:
            .  任意字符除(\n)
            ^  匹配开头
            $  匹配结尾
            [] 匹配指定的范围[abc][a-z][a-z*&￥]
           {m} 固定匹配m位
           {m,} >=m
           {m,n} x>=m x<=n
        正则预定义:
            \s  空白(空格)
            \b  边界
            \d  数字
            \w  word [0-9a-zA-Z_]
        大写反面 \S 非空格 \D 非数字.....

        '\w[0-9]' --> \w [0-9] 只能匹配一个字母

        量词：
            * >=0
            + >=1
            ? 0.1


        手机号码正则
            re.match['1[35789]\d{9}$',phone]

'''
import re

qq = input('输入qq号码：')
if len(qq) >= 5 and qq[0] != '0':
    print('qq是合法的')
else:
    print('qq不合法的')

# re模块中的match,从开头开始进行匹配若匹配不成功则返回None,匹配成功将会返回一个对象
msg = 'minguzimxlgsmlz'

pattern = re.compile('ming')
result = pattern.match(msg)  # 没有匹配成功返回None
print(result)

s = '刘洋风清扬张三丰天天'
res = re.match('风清扬', s)
print(res)

# re.search()
ress = re.search('风清扬', s)  # search() 进行正在字符串匹配方法，匹配的字符串
print(ress)
print(ress.span())  # span() 返回匹配的位置

print(ress.group())  # group() 提取到匹配的内容
print(ress.groups())

msgs = 'a7cdvb59hdks00789a'
rf = re.findall('[a-z][0-9]+[a-z]', msg)
print(rf)

# qq号码验证 5~11 开头不能是0
qqs = '730407639'
rm = re.match('^[1-9][0-9]{4,10}$', qqs)
print(rm)

# 正则验证用户登录
username = 'uzi007'
rt = re.match('^[a-zA-Z]\w{5,}$', username)
print(rt)

mags = 'aa*py ab.txt bb.py kk.png uu.py apyb.txt'
rfs = re.findall(r'\w*\.py\b', mags)
print(rfs)
