class dump(type):
    def __new__(metacls, name, parents, ns, **kwds):
        attr = {}
        for i in ns:
            if callable(ns[i]):
                def wrap1(f):
                    def wrap2(self, *args, **kwargs):
                        print(f'{f.__name__}: {args}, {kwargs}')
                        return f(self, *args, **kwargs)
                    return wrap2
                attr[i] = wrap1(ns[i])
            else:
                attr[i] = ns[i]
        return super().__new__(metacls, name, parents, attr, **kwds)


import sys
exec(sys.stdin.read())
