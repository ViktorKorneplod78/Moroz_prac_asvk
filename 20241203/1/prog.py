class dump(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = dict()
        for i, m in attrs.items():
            new_attrs[i] = m
            if callable(m):
                def wrap(m, i):
                    def wrapper(self, *args, **kwargs):
                        print(f"{i}: {args}, {kwargs}")
                        return m(self, *args, **kwargs)
                    return wrapper
                new_attrs[i] = wrap(m, i)
        return super().__new__(cls, name, bases, new_attrs)
import sys
exec(sys.stdin.read())
