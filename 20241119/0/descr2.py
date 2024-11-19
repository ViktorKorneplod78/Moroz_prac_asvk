class C:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 128: self._age = value
        else:
            print('Too old')
            raise ValueError
    @age.getter
    def age(self):
        if self._age == 42:
            print('Secret value')
            return -1
        else:
            return self._age
