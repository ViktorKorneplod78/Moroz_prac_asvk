def istype(typ):
    def deco(fun):
        def newfun(*args):
            if not all(isinstance(arg, typ) for arg in args):
                raise TypeError
            return fun(*args)
        return newfun
    return deco

@istype
def add(x, y, z):
    return x + y + z

