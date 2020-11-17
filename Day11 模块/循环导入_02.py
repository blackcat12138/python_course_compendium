def func():
    print('----->循环导入_02中的func函数--1--')
    from 循环导入_01 import test1
    test1()
    print('----->循环导入_02中的func函数--2--')
