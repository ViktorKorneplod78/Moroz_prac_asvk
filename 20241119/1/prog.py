def objcount(cls):
    cls.counter = 0

    og_init = cls.__init__
    def new_init(self, *args):
        cls.counter += 1
        og_init(self, *args)

    try:
        og_del = cls.__del__
    except:
        og_del = None
    def new_del(self):
        if callable(og_del):
            og_del(self)
        cls.counter -= 1

    cls.__init__ = new_init
    cls.__del__ = new_del
    return cls

import sys
exec(sys.stdin.read())
