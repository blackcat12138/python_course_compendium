# random模块
import random

# 获取0到1之间的随机小数
ran = random.random()
print(ran)

# 获取指定范围内的随机整数,默认步长为1
rans = random.randrange(1, 10, 2)  # randrange(start,stop,step)
print(rans)

ren = random.randint(1, 10)
print(ren)

# 在指定列表中随机获取列表中的元素
lists = ['uzi', 'mlxg', 'sofm', 'ming', 'tian']
rin = random.choice(lists)
print(rin)

# 将原列表中元素顺序打乱重新排序
pai = ['红桃A', '方块K', '梅花8', '黑桃J']
random.shuffle(pai)
print(pai)

'''
    练习：验证码 大写字母与数字的组合
'''


def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


code = func()
print(code)

print('----------------------------')
print(chr(65))  # Unicode码 ---> str
print(ord('A')) # str -->>Unicode码

print(ord('下'))
print(chr(19979))

# 标准模块中的函数:print() input() list() str() set() dir() int()