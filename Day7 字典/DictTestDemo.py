import random

lpls = dict(uiz='13', mlxg='14', sofm='12', xiye='14')
print(lpls)

lpl = {'uzi': '13', 'mlxg': '14', 'sofm': '12', 'xiye': '14'}
print(lpl.pop('uzi'))
print(lpl)

lck = {'uzi': '13', 'mlxg': '14', 'sofm': '12', 'xiye': '14'}
print([item for item in lck.items()])
print([key + '--' + value for key, value in lck.items()])

for i in lck.items():
    print(i)

print({x: random.randint(10, 100) for x in range(1, 5)})

name = ['绮梦', '冷伊一', '香凝', '黛兰']
sign = ['水瓶', '射手', '双鱼', '双子']
print({j: k + '座' for j, k in zip(name, sign)})
