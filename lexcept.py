#encoding: utf-8
'''了解，异常机制
'''
import sys
import traceback
import inspect
import timeit
from pprint import pprint

def errorer():
    raise ValueError('Error')

def test():
    return errorer()

def try_traceback():
    try:
        test()
    except Exception, e:
        pprint(sys.exc_info())
        pprint(traceback.extract_tb(sys.exc_info()[2]))

def try_inspect():
    try:
        test()
    except Exception, e:
        pprint(inspect.trace())


if __name__ == '__main__':
    print try_traceback()
    #print timeit.timeit(try_traceback, number=10000)
    #print timeit.timeit(try_inspect, number=10000)
