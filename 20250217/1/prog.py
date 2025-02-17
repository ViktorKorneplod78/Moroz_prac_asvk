from zlib import decompress
from glob import iglob
from os.path import dirname, basename
import sys

print('\n'.join([basename(i) for i in iglob(sys.argv[1] + "/.git/refs/heads/*")]))
