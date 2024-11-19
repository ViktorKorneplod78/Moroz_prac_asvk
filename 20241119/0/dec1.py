def dumper(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@dumper
def fun(a,b):
    return a*2+b

@dumper
def isint(*args):
    for i in args:
        if type(i) != type(1):
            raise TypeError
    return True

print(isint(2,'sdfs'))
