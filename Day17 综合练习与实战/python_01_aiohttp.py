'''
   [01]、python中最好用的异步爬虫库aiohttp代码实例
    aiohttp被分为服务器端和客户端
'''
import asyncio
import aiohttp


async def aiohttp_test01(ur1):
    # 创建clientSession对象命名为session
    async with aiohttp.ClientSession() as session:
        # session的get方法得到一个clientResponse对象命名为resp
        async with session.get(ur1) as resp:
            print(resp.status)
            print(await resp.text())


loop = asyncio.get_event_loop()
tasks = [aiohttp_test01("https://api.github.com/events")]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
