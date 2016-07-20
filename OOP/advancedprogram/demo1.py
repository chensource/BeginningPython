class Student(object):
    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

# def __getattr__(self, attr):
#     if (attr == "score"):
#         return 99

    def __getattr__(self, attr):
        if (attr == "score"):
            return 99
        if attr == "age":
            return lambda: 25
        raise AttributeError(" \'Student\' object has no attribute \'%s\'" %
                             attr)

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):  #如果是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  #如果是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# for n in Fib():
#     print(n)

# f = Fib()
# print(f[0:5])
#
# s = Student()
# print(s.score)
#
# print(s.age())

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self.path
#
#     __repr__ = __str__

# link = Chain().status.users('chenshi2').timeline.list

# print(link)

# from enum import Enum, unique
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
#                        'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, "=>", member, ",", member.value)
#
#
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# # day1=Weekday.Fri
# print(Weekday["Tue"])
#
# # print(day1 == Weekday.Fri)
# print(Weekday(1))
#
# for name, member in Weekday.__members__.items():
#     print(name, "=>", member)
