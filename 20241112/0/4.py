C = type("C", (), {"a": 100500, "__init__": lambda self, val: setattr(self, "a", val), "fun": lambda self: self.a})
c = C(2)
print(c.__dict__)
