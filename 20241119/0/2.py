def istype(typ):
    def deco(fun):
        def newfun(*args):
            if not all(isinstance(arg, typ) for arg in args):
                raise TypeError(f"not all {typ}")
            return fun(*args)
        return newfun
    return deco

@istype(int)
def fun(a,b):
    return a*2+b

print(fun(2,3))
