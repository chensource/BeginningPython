from collections import namedtuple
from collections import deque
from collections import defaultdict

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
#
# print("p.x = %s" % p.x)
# print("p.y = %s" % p.y)
#
# print(isinstance(p, tuple))

# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
#
# print(q)

# dd = defaultdict(lambda:'N/A')
# dd['key'] = 'abc'
# print(dd['key'])
# print(dd['key2'])

from collections import OrderedDict


class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('Remove', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


d = LastUpdateOrderedDict(2)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)
