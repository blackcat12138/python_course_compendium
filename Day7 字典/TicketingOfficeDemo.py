# 封装售票机对象
class Ticketing_machine:
    # 初始化方法
    def __init__(self):
        print('\n欢迎使用自动售票机~~')
        pass
    # 选择电影
    def Films(self,Films_name):
        Ticketing_machine.Films_name=Films_name
        print('已选电影：'+Films_name)
        pass
    # 选择电影场次
    def Movie_fields(self,Movie_field):
        Ticketing_machine.Movie_field="2018.4.12"+Movie_field
        print('电影场次：'+Movie_field)
    # 选择座位
    def seats(self,seat):
        Ticketing_machine.seat = seat
        print('选择座位：'+seat)
    # 打印电影票
    def Cinema_ticket(self):
        print("电影："+Ticketing_machine.Films_name)
        print("播出时间："+Ticketing_machine.Movie_field)
        print("座位："+Ticketing_machine.seat)
# 初始化售票机对象
ticketing=Ticketing_machine()
# 提示正在上映电影
print('\n请选择正在上映的电影：1、《环太平洋：雷霆再起》  2、《头号玩家》  3、《红海行动》')
# 选择的电影
ticketing.Films('《头号玩家》')
# 提示选择的场次
print('\n请选择电影播放场次：1、9:30  2、10:40  3、12:00')
# 选择的场次
ticketing.Movie_fields('10:40')
# 提示选择座位
print('\n请选择座位剩余座位：10-01,10-02,10-03,10-04')
# 选择的座位
ticketing.seats('10-3')
print('\n正在出票。。。\n')
# 电影票信息
ticketing.Cinema_ticket()
print('\n出票完成，请别忘记取票')