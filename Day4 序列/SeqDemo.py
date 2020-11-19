verse = ["春眠不觉晓", "Python不得了", "夜来爬数据", "好评知多少", "java算神马", "C才是大爷", "TES牛逼"]
print(verse[2])
print(verse[-1])
print(verse[1:2])
print(verse[:7:2])

print("春眠不觉晓" in verse)
print("春眠不觉晓" not in verse)

print('-' * 20)

# 支持赋值给多个变量
items = [1, 2, 3, 4, 5]
a, *_, b = items
print(*_)
