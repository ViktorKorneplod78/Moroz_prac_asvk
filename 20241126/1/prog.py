import sys
instr = sys.stdin.buffer.read()
N, tail = instr[0], instr[1:]
L = len(tail)

parts = []
for i in range(N):
    parts.append(tail[int(i*L/N):int((i+1)*L/N)])

parts.sort()
res = bytes([N]) + b''.join(parts)
sys.stdout.buffer.write(res)
