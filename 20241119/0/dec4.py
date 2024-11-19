class Sender:
    cnt = True
    @classmethod
    def report(cls):
        if cls.cnt:
            cls.cnt = False
            return 'Greetings'
        return 'Get away'

class Asker:
    @staticmethod
    def askall(lst):
        return [i.report() for i in lst]

s = Sender()
print(s.report())
print(s.report())
lst = [Sender() for i in range(5)]
a = Asker()
print(Asker().askall(lst))
