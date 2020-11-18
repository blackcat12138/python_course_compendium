'''
    线程的创建

'''
import threading
from time import sleep


def downloand(n):
    images = ['girl.jpg', 'boy.jpg', 'men.jpg']
    for images in images:
        print('正在下载:', images)
        sleep(0.5)
        print('下载{}成功:'.format(images))


def listenMusic():
    musics = ['冰雨', '桥边菇凉', '烤面筋']
    for music in musics:
        sleep(0.5)
        print('正在听{}歌！:'.format(music))


if __name__ == '__main__':
    # 创建线程对象
    t1 = threading.Thread(target=downloand, name='uzi', args=(1,))
    t1.start()

    t2 = threading.Thread(target=listenMusic, name='ming')
    t2.start()

    n = 1
    while True:
        print(n)
        sleep(1)
        n += 1
