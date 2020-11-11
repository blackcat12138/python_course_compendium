# 自定义判断选项方法x和y分别代表输入的内容和总字数
def check(x, y):
    # 捕捉转换类型错误异常
    try:
        # 转换输入内容类型
        x = int(x)
    # 错误执行的方法
    except:
        # 输入错误重新提示用户输入
        input("您输入的套餐不存在请重新输入：")
        # 重新启动检测错误方法
        return check(x, y)
    # 检测输入的是在范围内
    if x > 0 and x <= y:
        # 在范围内返回
        return x
    else:
        # 不在范围内提示用户重新输入
        x = input("您输入的套餐不存在请重新输入：")
        # 重新启动检测方法
        return check(x, y)


# 可设置话费列表
Bill_sets = ['0分钟', '50分钟', '100分钟', '300分钟', '不限量']
# 可设置流量列表
flow_sets = ['0M', '500M', '1G', '5G', '不限量']
# 可设置短信列表
sms_sets = ['0条', '50条', '100条']
# 控制台输出提示
print('定制自己的手机套餐：')
# 通话设置
print('{}\n{}\n{}\n{}\n{}\n{}'.format('A.请设置通话时长：',
                                      "1." + Bill_sets[0],
                                      "2." + Bill_sets[1],
                                      "3" + Bill_sets[2],
                                      "4" + Bill_sets[3],
                                      "5" + Bill_sets[4]
                                      ))
# 提示用户输入选择通话时间
Aset = input("请输入选择的通话时间编号：")
# 检查输入内容的合法性 并返回正确内容
Aset = check(Aset, 5)
# 提示用户设置流量
print('\n{}\n{}\n{}\n{}\n{}\n{}'.format('B.请设置流量：',
                                        "1." + flow_sets[0],
                                        "2." + flow_sets[1],
                                        "3." + flow_sets[2],
                                        "4." + flow_sets[3],
                                        "5." + flow_sets[4]
                                        ))
# 提示用户输入选择流量
Bset = input("熟人选择的通话时间编号：")
# 检查输入内容的合法性 并返回正确内容
Bset = check(Bset, 5)
# 提示用户设置短信条数
print('\n{}\n{}\n{}\n{}'.format('C.请设置短信条数：',
                                "1." + flow_sets[0],
                                "2." + flow_sets[1],
                                "3." + flow_sets[2]
                                ))
# 提示用户输入选择短信条数
Cset = input("输入选择的通话时间编号：")
# 检测输入内容的合法性 并返回正确内容
Cset = check(Cset, 3)
print('\n您的手机套餐定制成功：免费通话时长为：' + Bill_sets[Aset - 1] + '/月,流量为'
      + flow_sets[Bset - 1] + '/月,短信条数为'
      + sms_sets[Cset - 1] + '/月'
      )
