def dumper(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

def isint(f):
    def a(*args):
        for arg in args:
            if type(arg) != int:
                raise TypeError
        return f(*args)
    return a

@dumper
@isint
def fun(a,b):
    return a*2+b

print(fun("b",3))
