# 检查是否有该车次方法
def check_train_number(string):
    # 检查某个元素是否是列表的成员 检查输入的车次是否包含在车次系列中
    if string in train_numbers:
        # 包含在车次系列中退出方法
        return string
    else:
        # 输出不包含在车次系列中,提示用户再次输入
        y = input("没有该车次,请重新输入要购买的车次：")
        # 检查输入的车次是否存在在车次系列中
        return check_train_number(y)


type = ['车次', '出发站-到达站', '出发时间', '到达时间', '历时']
# 车次列表
train_numbers = ['T40', 'T298', 'Z158', 'Z62']
# 出发站-到达站列表
DepartureStation_ArrivalStation = ['长春-北京', '长春-北京', '长春-北京', '长春-北京']
# 出发时间列表
Departure_time = ['00:12', '00:06', '12:48', '21:58']
# 到达时间类别
Arrival_time = ['12:20', '10:44', '08:18', '8:20']
# 用是列表
Duration = ['12:08', '10:44', '08:18', '8:20']
# 输出火车票信息
print('{} {} {} {} {}'.format(type[0], type[1], type[2], type[3], type[4]))
print('{} {} {} {} {}'.format(train_numbers[0], DepartureStation_ArrivalStation[0], Departure_time[0], Arrival_time[0],
                              Duration[0]))
print('{} {} {} {} {}'.format(train_numbers[1], DepartureStation_ArrivalStation[1], Departure_time[1], Arrival_time[1],
                              Duration[1]))
print('{} {} {} {} {}'.format(train_numbers[2], DepartureStation_ArrivalStation[2], Departure_time[2], Arrival_time[2],
                              Duration[2]))
print('{} {} {} {} {}'.format(train_numbers[3], DepartureStation_ArrivalStation[3], Departure_time[3], Arrival_time[3],
                              Duration[3]))
# 提示用户虚入车次
train_number = input("请输入要购买的车次：")
# 检查输入的车次是否包含在列表中,接受正确的车次
train_number = check_train_number(train_number)
# 提示用户输入乘车人信息
user_rider = input("请输入乘车人(用逗号分隔)：")
# 判断购买的是那个车次，根据选购的车次判断出发时间
if train_number == train_numbers[0]:
    time = Departure_time[0]
if train_numbers == train_numbers[1]:
    time = Departure_time[1]
if train_numbers == train_numbers[2]:
    time = Departure_time[2]
if train_numbers == train_numbers[3]:
    time = Departure_time[3]
print('你已购' + train_number + '次列车 长春-北京' + time + '开,请' + user_rider + '尽快换取车票。【铁路客服】')
