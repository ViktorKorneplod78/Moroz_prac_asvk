from zlib import decompress
from glob import iglob
from os.path import dirname, basename
import sys

path = sys.argv[1]

if len(sys.argv) == 2:
    print('\n'.join([basename(i) for i in iglob(path + "/.git/refs/heads/*")]))
else:
    comm_id = open(path + '/.git/refs/heads/' + sys.argv[2]).read()[:-1]
    obj = decompress(open(path + f'/.git/objects/{comm_id[:2]}/{comm_id[2:]}', 'rb').read())
    print(obj.partition(b'\x00')[2].decode(), end = "")
