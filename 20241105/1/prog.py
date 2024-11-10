class Omnibus:
    attrs = dict()

    def __setattr__(self, name, value):
        if name not in self.__dict__:
            super().__setattr__(name, value)
            if name in Omnibus.attrs:
                Omnibus.attrs[name] += 1
            else:
                Omnibus.attrs[name] = 1

    def __getattribute__(self, name):
        if name[0] != '_':
            return Omnibus.attrs.get(name, 0)
        else:
            return super().__getattribute__(name)

    def __delattr__(self, name):
        if name in self.__dict__:
            super().__delattr__(name)
            Omnibus.attrs[name] -= 1

import sys
exec(sys.stdin.read())
