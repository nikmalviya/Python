from time import time


class StopWatch:
    def __init__(self):
        self.__start_time = time()
        self.__end_time = 0

    def start(self):
        self.__start_time = time()

    def stop(self):
        self.__end_time = time()

    def get_elapsed_time(self):
        return self.__end_time - self.__start_time

    def get_start_time(self):
        return self.__start_time

    def get_end_time(self):
        return self.__end_time


if __name__ == '__main__':
    timer = StopWatch()
    timer.start()
    s = 0
    for i in range(1, 1000000):
        s += i
    timer.stop()
    print('Elapsed Time : {:.2f}ms'.format(timer.get_elapsed_time()))
