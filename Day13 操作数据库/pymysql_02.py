'''
    pymysql操作mysql中的查询
'''
import pymysql


def main():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='rpt_ods',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute('select stuid,stunm from student')
            # for row in cursor.fetchall():
            #     print(f'学生编号：{row[0]}')
            #     print(f'学生名称：{row[1]}')
            #     print('-'*20)
            print(cursor.fetchall())
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
    print('测试连接：', conn)


if __name__ == '__main__':
    main()
