#encoding: utf-8
'''了解staticmethod和classmethod, 区别查看http://pythoncentral.io/difference-between-staticmethod-and-classmethod-in-python/
'''

class Zoo(object):
    country = 'China'

    def __init__(self):
        self.name = 'CrazyZoo'

    @classmethod # 目的是操作类的成员变量, 不管是实例调用还是类调用, 第一个参数都是类
    def print_country(cls):
        print 'country is: ', cls.country

    @staticmethod # 普通函数, 与类和实例无关, 不需要第一个参数是self or cls
    def print_static(*args):
        print 'Static: ', args

    def print_name(self):
        print 'name is: ', self.name

if __name__ == '__main__':
    z = Zoo()
    z.print_name()
    z.print_country()
    z.print_static()
    Zoo.print_static()
