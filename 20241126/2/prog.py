import sys

buf = sys.stdin.read()
print(buf.encode('latin1', errors='replace').decode('CP1251', errors='replace'))
