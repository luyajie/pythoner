# Python len

------

>* python的字符串有两种类型, str和unicode
>* len(str)获取str的字节数, str有ascii编码、utf8编码等, 不同编码会有不同的字节数, 例如: len('a')=1, len('中')=3
>* len(unicode)获取unicode的字符数, unicode一般就2个字节, 特殊的有4个字节, 例如: len(u'中')=1
