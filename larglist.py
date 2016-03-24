#encoding: utf8
'''了解，参数默认empty list
'''

if __name__ == '__main__':
    def test(val, l=[]):
        l.append(val)

        #print l
        return l

    l1 = test(10)
    l2 = test(20, [])
    l3 = test(30)

    print l1
    print l2
    print l3
