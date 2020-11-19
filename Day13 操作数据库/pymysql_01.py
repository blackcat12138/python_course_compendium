'''
    通过python程序实现对mysql数据库的uird操作,
    通过pymysql模块实现对数据库的相关操作,若出现上万条数据的修改、查询、更新、删除操作,
    代码将会冗余,并且代码耦合性太强了,不便于维护。
'''
import pymysql


def main():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='rpt_ods',
        charset='utf8'
    )
    try:
        with conn.cursor() as cursor:
            result = cursor.execute(
                'insert into student values(2000,"张青")'
            )
            if result == 1:
                print('插入成功！')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
    print('测试连接：', conn)


if __name__ == '__main__':
    main()
