'''
    循环导入：在大型的python项目中,需要很多python文件,由于架构不当,可能会出现模块间的相互导入
            A: 模块
                def test()
                    f()
            B: 模块
                def f()
                    test()
    避免产生循环导入的方式：
        1.重新架构
        2.将导入的语句放在函数中
        3.将导入语句放到模块的最后
'''
from 循环导入_02 import func


def test1():
    print('------>test1')


def test2():
    print('----------->test2')
    func()


test1()
test2()

# if __name__ == '__main__':
#     # 调用tast1
#     test1()
#     test2()


