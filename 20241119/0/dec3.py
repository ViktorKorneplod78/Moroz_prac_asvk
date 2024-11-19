class istype:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def newf(*args):
            if not all(isinstance(arg, self.typ) for arg in args):
                raise TypeError
            return fun(*args)
        return newf

@istype(int)
def add(x,y,z):
    return x + y + z

print(add(1, 2, 3))
