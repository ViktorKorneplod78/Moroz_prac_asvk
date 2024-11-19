class IsType():
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def newfun(*args):
            if not all(isinstance(arg, self.typ) for arg in args):
                raise TypeError(f"not all {self.typ}")
            return fun(*args)
        return newfun

@IsType(int)
def add(x, y, z):
    return x + y + z

print(add("f", 2, 3))
