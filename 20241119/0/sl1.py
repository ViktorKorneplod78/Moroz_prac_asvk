class slo:

    __slots__ = "a", "b", "c"
    readonly = 100500

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c


from string import ascii_letters
class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

class Slotter:
    __slots__ = (i for i in ascii_letters)

