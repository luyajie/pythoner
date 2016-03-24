#encoding: utf-8
'''了解，装饰器
'''
import functools

def current_id():
    return 1

def get_permissions(id):
    return ['login']

def require(permission):
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            permissions = get_permissions(current_id())
            if permission in permissions:
                return func(*args, **kwargs)
            else:
                raise Exception('Not allowed!')
        return decorated
    return decorator

@require('login')
def view_friend():
    print "into view friend"

@require('login')
def del_picture():
    print "into del picture"

def complex_test():
    view_friend()
    print view_friend.__name__
    del_picture()

def say_more(func):
    def wrap(*args, **kwargs):
        print 'I love python! '
        return func(*args, **kwargs)

    return wrap

@say_more
def say_hello():
    print "hello"

def simple_test():
    say_hello()
if __name__ == '__main__':
    #complex_test()
    simple_test()
