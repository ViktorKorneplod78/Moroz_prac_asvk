class Omnibus:
    exempl = {}
    def __setattr__(self, attr, n):
        if attr in Omnibus.exempl:
            Omnibus.exempl[attr].add(self)
        else:
            Omnibus.exempl[attr] = set([self])

    def __getattribute__(self, attr):
        if attr in Omnibus.exempl:
            return len(Omnibus.exempl[attr])
        return 0

    def __delattr__(self, attr):
        if attr in Omnibus.exempl:
            Omnibus.exempl[attr].discard(self)

import sys
exec(sys.stdin.read())
