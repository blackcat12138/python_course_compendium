# 案例一
print("2017~2018赛季NBA西部联盟前八名：")
teams = ["休斯顿 火箭", "金州 勇士", "波特兰 开拓者", "犹他 爵士", "新奥尔良 鹈鹕",
         "圣安东尼奥 马刺", "俄克拉荷马城 雷霆", "明尼苏达 森林狼"]
# for tea in teams:
#     print(tea)
sales = [tea for tea in teams]
print(sales)

# 案例二
print("===============================")
for inde, ite in enumerate(teams):
    print(inde + 1, ite)

# 案例三
print("============================")
for int, it in enumerate(teams):
    if int % 2 == 0:
        print(it + "\t\t", end='')
    else:
        print(it + "\n")

# 案例四
print("==========================")
grade = [99, 97, 98, 91, 100, 101, 95]
print("原列表：", grade)
print(grade.sort())  # None
grade.sort()
print("升序1：", grade)
print("升序2：", sorted(grade))

# 案例五
print("==========================")
price = [1200, 5330, 2988, 6200, 1998, 8888]
sale = [x * 0.5 for x in price]
print("打五折的价格：", sale)

# 案例六
print("==========================")
str1 = "千山鸟飞绝"
str2 = "万径人踪灭"
str3 = "孤舟蓑笠翁"
str4 = "独钓寒江雪"
verse = [list(str1), list(str2), list(str3), list(str4)]
print("\n-- 横版 --\n")
for i in range(4):
    for j in range(5):
        if j == 4:
            print(verse[i][j])
        else:
            print(verse[i][j], end="")
verse.reverse()
print("\n-- 竖版 --\n")
for i in range(5):
    for j in range(4):
        if j == 3:
            print(verse[j][i])
        else:
            print(verse[j][i], end="")
