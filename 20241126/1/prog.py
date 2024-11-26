import sys

buf = sys.stdin.buffer
n_byte = buf.read(1)
n = int.from_bytes(n_byte)
tail = buf.read().decode()
l = len(tail)
output = []
for i in range(n):
    output.append(tail[i * l // n:(i + 1) * l // n])
sys.stdout.buffer.write(n_byte)
for i in sorted(output):
    sys.stdout.buffer.write(i.encode())
