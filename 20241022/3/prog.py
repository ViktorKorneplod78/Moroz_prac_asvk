from itertools import *
print(*sorted(list(filter(lambda s: s.count("TOR") == 2, [''.join(list(i)) for i in product(['T', 'O', 'R'], repeat = int(input()))]))), sep = ', ')
