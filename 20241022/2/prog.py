from itertools import *
def slide(seq, n):
    begin = 0
    end = n
    for win in tee(seq, len(seq)):
        yield from islice(win, begin, min(end, len(seq)))
        begin += 1
        end += 1
import sys
exec(sys.stdin.read())
