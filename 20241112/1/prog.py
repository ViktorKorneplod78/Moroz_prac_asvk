from collections import UserString
class DivStr(UserString):
    def __init__(self, data = ''):
        super().__init__(data)
    def __floordiv__(self, n):
        m = len(self.data) // n
        for i in range(n):
            yield self.data[i * m:(i + 1) * m]
    def __mod__(self, n):
        l = len(self.data)
        return DivStr(self.data[l - l % n:])
import sys
exec(sys.stdin.read())
