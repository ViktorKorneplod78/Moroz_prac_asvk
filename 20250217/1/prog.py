from zlib import decompress
from glob import iglob
from os.path import dirname, basename
import sys

def get_obj(path, obj_id):
    return decompress(open(path + f'/.git/objects/{obj_id[:2]}/{obj_id[2:]}', 'rb').read()).partition(b'\x00')

def tree_walkthrough(path, body):
    tree = []
    tail = body
    while tail:
        treeobj, _, tail = tail.partition(b'\x00')
        tmode, tname = treeobj.split()
        num, tail = tail[:20], tail[20:]
        obj_id = num.hex()
        obj_name = get_obj(path, obj_id)[0].decode().split()[0]
        tree.append([obj_name, obj_id, tname.decode()])
    return tree

path = sys.argv[1]

if len(sys.argv) == 2:
    # 1st
    print('\n'.join([basename(i) for i in iglob(path + "/.git/refs/heads/*")]))
elif len(sys.argv) == 3:
    branch = sys.argv[2]
    comm_id = open(path + '/.git/refs/heads/' + branch).read()[:-1]
    comm_body = get_obj(path, comm_id)[2]
    # 2nd
    print(comm_body.decode(), end = "")

    # 3d
    tree_id = comm_body.decode().split('\n')[0].split()[1]
    header, _, body = get_obj(path, tree_id)
    print('\n'.join([' '.join(i) for i in tree_walkthrough(path, body)]), end = ' ')

    #4 th
    comm_dict = dict()
    for i in open(path+'/.git/logs/refs/heads/' + branch).read().split('\n'):
        if len(i) == 0: continue
        curr = i.split()[1]
        if curr not in comm_dict:
            comm_dict[curr] = i.split()[0]
    curr = comm_id
    while curr != '0000000000000000000000000000000000000000':
        print(f'TREE for commit {curr}')
        curr = commits[curr]
        header, _, body = get_obj(path, body.decode().split('\n')[0].split()[1][2].decode().split('\n')[0].split()[1])
        print('\n'.join([' '.join(i) for i in parse_tree(path, body)]))
else:
    print("what")
