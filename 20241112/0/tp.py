C = type('C', tuple(), {'a': 100, 'fun': lambda self:self.a, '__init__': lambda self, n: setattr(self, 'a', n)})
