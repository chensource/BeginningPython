# import time, threading
#
#
# #新线程执行的代码
# def loop():
#     print('thread %s is running....' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#         time.sleep(1)
#     print("thread %s ended." % threading.current_thread().name)
#
#
# print("thread %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print("thread %s ended." % threading.current_thread().name)

# import time, threading
#
# BLANCE = 0
# Lock = threading.Lock() #锁
#
#
# def change_it(n):
#     global BLANCE
#     BLANCE = BLANCE + n
#     BLANCE = BLANCE - n
#
#
# def run_thred(n):
#     for i in range(100000):
#         Lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             Lock.release() #释放
#
#
# t1 = threading.Thread(target=run_thred, args=(5, ))
# t2 = threading.Thread(target=run_thred, args=(8, ))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(BLANCE)

# import threading, multiprocessing
#
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# print(multiprocessing.cpu_count())
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print("hello,%s(in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()

t1.join()
t2.join()
