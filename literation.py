#coding: utf-8
'''了解，迭代器
'''

class Data(object):
    def __init__(self, *args):
        self._data = args
        self._index = 0

    def __iter__(self):
        return self

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()

        result = self._data[self._index]
        self._index += 1

        return result


if __name__ == '__main__':
    obj = Data(1, 2, 3)

    for d in obj:
        print d
