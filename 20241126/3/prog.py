import sys
def b_to_i(b):
    return int.from_bytes(b, 'little')
try:
    f = sys.stdin.buffer.read()
    if any((f[:4] != b'RIFF', f[8:12] != b'WAVE', f[12:16] != b'fmt ', b_to_i(f[16:20]) != 16)):
        raise Exception
    print(f"Size={b_to_i(f[4:8])}", f"Type={b_to_i(f[20:22])}", f"Channels={b_to_i(f[22:24])}", f"Rate={b_to_i(f[24:28])}", f"Bits={b_to_i(f[34:36])}", f"Data size={b_to_i(f[40:44])}", sep = ", ")
except:
    print("NO")
