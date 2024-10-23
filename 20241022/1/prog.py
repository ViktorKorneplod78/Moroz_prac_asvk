def fib(m, n):
    a, b = 1, 1
    if m == 0 and n > 0:
        yield 1
    for i in range(1, m + n):
        if i >= m:
            yield b
        a, b = b, a + b
import sys
exec(sys.stdin.read())
