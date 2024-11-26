import pickle

class SerCls:
    def __init__(self):
        self.lst = list(a, b, c)
        self.dct = {'a': a, 'b': b, 'c': c}
        self.st = f'{a} {b} {c}'

    def __str__(self):
        return self.lst, self.dct, self.st)
