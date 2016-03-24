#encoding: utf-8
'''了解，多线程与多进程
'''
import os
import math
import arrow
import time
import multiprocessing
from threading import Thread
from Queue import Queue, Empty

from tools import seconds_to_human


START, STOP, STEP = 100000, 1000000, 100000

def is_prime(n):
    if n < 2: return False

    i, max = 2, int(math.ceil(math.sqrt(n)))

    while i <= max:
        if n % i == 0: return False
        i += 1

    return True

def sum_prime(n):
    return sum([x for x in xrange(2, n) if is_prime(x)])

def single_thread():
    print 'single_thread start: %s' % seconds_to_human(time.time())

    for i in xrange(START, STOP, STEP):
        print sum_prime(i)

    print 'single_thread end: %s' % seconds_to_human(time.time())

def do_work(q):
    while True:
        try:
            x = q.get(block=False)
            print sum_prime(x)
        except Empty:
            break

def multi_thread():
    print 'multi_thread start: %s' % seconds_to_human(time.time())

    work_queue = Queue()

    for i in xrange(START, STOP, STEP):
        work_queue.put(i)

    threads = [Thread(target=do_work, args=(work_queue, )) for i in range(8)]

    [t.start() for t in threads]
    [t.join() for t in threads]

    print 'multi_thread end: %s' % seconds_to_human(time.time())

def multi_process():
    print 'multi_process start: %s' % seconds_to_human(time.time())

    work_queue = multiprocessing.Queue()

    for i in xrange(START, STOP, STEP):
        work_queue.put(i)

    processes = [multiprocessing.Process(target=do_work, args=(work_queue, )) for i in range(8)]

    [t.start() for t in processes]
    [t.join() for t in processes]

    print 'multi_process end: %s' % seconds_to_human(time.time())


test_list = [4, -7, 3, -2, -6, 14, -11, 14, -7, -3, 2, 8, -15, 7, 0, 9, -18, 11, 7, -1, -2, 0, -1, -15, 1, 11, -10, 17, -2, -4, -5, -7, 18, -20, 20, -7, 1, 1, 3, -9, 1, -2, -6, 10, 1, -6, 3, -1, -3, -5, 8, 8, 1, -18, 11, -7, 1, 15, -7, -11, 4, 1, 6, 1, -4, -5, 2, 0, 11, -18, 16, -2, 1, -4, -7, 1, 5, 2, 0, 8, -5, -8, 10, -4, 7, -17, 10, 4, -6, -8, 13, -13, 14, 3, -2, 2, -15, -4, 19, -3, 0, -15, 0, 6, -3, 6, 6, -17, 16, 3, -14, 8, -3, 3, -4, -7, -1, 13, -3, 1, -10, 4, -4, 10, -10, 10, -2, -7, 5, -7, 1, 18, -9, -11, 15, -1, -7, -1, 1, 4, -5, 8, -9, -3, 4, 5, -8, 9, -2, -3, -4, 11, -1, -1, 7, -19, 16, -16, 15, -15, 10, 5, -12, 4, 6, -8, -3, 9, -6, 3, -8, 1, 9, -10, 18, -11, 4, 2, -12, 6, 11, -3, -13, 10, -12, 19, -14, -2, 3, 7, -13, 19, -19, 5, 6, 6, -3, 6, -2, -17, 6, -1, 11, -5, 1, 7, -15, 12, 0, -3, -12, -2, 17, -11, 9, -11, 15, -15, 2, 0, 3, 9, -3, 5, -6, 0, -6, 0, 2, -9, 18, -2, -6, 0, -3, 0, -7, 7, -4, 10, -11, 1, 10, -8, 10, -11, 8, -9, 8, -10, 8, -8, 17, -11, -1, -2, 14, -12, 4, 9, -18, 12, -5, -5, 8, -6, 6, 6, -8, 8, -6, -10, 13, -13, 11, -2, -2, 9, -4, -1, 2, -15, 2, 14, 1, -5, -6, -5, 9, -4, 1, -3, 11, -1, 6, -15, 7, 8, -14, 11, -8, -3, 13, 1, 0, -6, -13, 2, 11, -14, 14, 5, -14, 5, 6, -14, 3, -3, 9, 7, -6, -3, 7, -16, 5, 11, -11, 2, 13, -9, -8, -3, 6, 7, 2, -3, 0, -3, -6, 12, -12, 13, -13, 12, 1, -11, -3, 8, 3, -5, 12, -2, -13, -3, -1, 2, 16, -3, 3, -1, -16, 8, 8, -18, 1, 13, -9, 6, 6, -4, -1, 8, -10, 7, -2, -5, 4, 3, -17, 18, -15, 3, 7, 1, -1, -8, 2, 0, 13, -2, -5, -8, 11, -7, -8, 6, 4, 1, 4, -2, 0, 1, -7, 8, -5, -8, 1, -2, 2, -1, 6, -4, 7, -10, 1, 7, 1, -6, -2, 15, -4, -12, 0, 8, 3, 6, -8, 0, -1, -3, -7, 4, 5, 3, -11, 13, -2, 0, -3, -5, 2, 0, 0, -5, 1, 9, 0, 6, -2, 1, 0, -15, 11, 5, 1, 0, -17, 15, -4, -8, 1, -2, 5, 6, -9, 2, 13, -14, 3, 6, -10, 8, 2, 2, 0, -2, -1, -1, 0, -12, 14, -7, 10, -14, 11, -2, -5, 2, 7, -6, 0, -7, 8, -11, 4, 11, -2, 4, -6, 5] * 5
def sum_zero(step_queue):
    count = 0

    while 1:
        try:
            step = step_queue.get(block=False)

            for i in xrange(len(test_list) - step):
                if sum(test_list[i:i+step+1]) == 0:
                    count += 1
        except Empty:
            if step_queue.empty(): break

def multiprocess_sum_zero():
    start_time = seconds_to_human(time.time())

    step_queue = multiprocessing.Queue()

    for i in xrange(len(test_list) - 1):
        step_queue.put(i)

    processes = [multiprocessing.Process(target=sum_zero, args=(step_queue, )) for i in range(8)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print 'multi_sum_zero start: %s' % start_time
    print 'multi_sum_zero end: %s' % seconds_to_human(time.time())

def single_sum_zero():
    start_time = seconds_to_human(time.time())

    count = 0
    for step in xrange(len(test_list)):
        for i in xrange(len(test_list) - step):
            if sum(test_list[i:i+step+1]) == 0: count += 1

    print 'single_sum_zero count: %s' % count
    print 'single_sum_zero start: %s' % start_time
    print 'single_sum_zero end: %s' % seconds_to_human(time.time())

def pool_sum_zero(step):
    count = 0

    for i in xrange(len(test_list) - step):
        if sum(test_list[i:i+step+1]) == 0:
            count += 1

    return count

def multiprocess_pool_sum_zero():
    result = []
    count = 0
    start_time = seconds_to_human(time.time())
    p = multiprocessing.Pool(8)

    for i in xrange(len(test_list) - 1):
        result.append(p.apply_async(pool_sum_zero, (i, ))) # async实现异步, apply和map区别在于: apply可以多个函数, map同一个函数和iterator

    p.close()
    p.join()

    for res in result:
        count += res.get()

    print 'pool_sum_zero count: %s' % count
    print 'pool_sum_zero start: %s' % start_time
    print 'pool_sum_zero end: %s' % seconds_to_human(time.time())

if __name__ == '__main__':
    #single_thread()
    #multi_thread()
    #multi_process()

    #single_sum_zero()
    #multiprocess_sum_zero() # queue 更多用于进程通信
    multiprocess_pool_sum_zero() # pool 方便创建多进程和得到子进程的返回值
