import threading
import time
'''
Semaphore 机制测试
'''
class Process(threading.Thread):
    def __init__(self, name, sem):
        super().__init__(name=name)
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('{} is processed.'.format(self.name))
        self.sem.release()

class Scrapy(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(15):
            self.sem.acquire()
            prc = Process("http://www.google.com?id={}".format(i), self.sem)
            prc.start()

if __name__ == '__main__':
    sem = threading.Semaphore(3)
    scrapy = Scrapy(sem)  # 每次 3 个线程
    scrapy.start()