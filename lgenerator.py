#encoding: utf-8
'''了解，生成器
'''
import time

def g_expression():
    g = (x for x in [1, 2, 3])
    print g


def g_object():
    class Data(object):
        def __init__(self, *args):
            self._data = list(args)

        def __iter__(self):
            for x in self._data:
                yield x

    g = Data(1, 2, 3)
    print g

def g_function():
    def transfer_to_generator(l):
        for x in l:
            yield x

    g = transfer_to_generator([1, 2, 3])
    print g

def g_producer_consumer():
    def consumer():
        result = 'Init'
        while True:
            n = yield result # magic
            if not n: return
            print '[Consumer start] %s' % n
            result = '200 ok'

    def producer(c):
        r = c.next() # consumer运行到magic -> consumer返回r值(Init) -> consumer停止, consumerc.send(None) 一样
        n = 5
        while n > 0:
            print '[Producer start] %s' % n
            ack = c.send(n)
            print '[Consumer ack  ] %s' % ack
            print '-' * 100
            n -= 1
        c.close()

    producer(consumer())

if __name__ == '__main__':
    g_expression() # 生成器表达式
    g_object()     # 生成器对象
    g_function()   # 生成器函数
    g_producer_consumer() # 生成器协
