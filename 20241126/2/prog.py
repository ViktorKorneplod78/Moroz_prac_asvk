import sys
sys.stdout.buffer.write(sys.stdin.buffer.read().decode('utf-8', errors = 'replace').encode('latin1', errors = 'replace'))
