class Student(object):
    # 用tuple 定义允许绑定的属性名称
    # __slots__ = ("name", "age", "score")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("score must be integer")
        if value < 0 or value > 100:
            raise ValueError("value must between 0-100")
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth

    pass

#
# s = Student()
# s.score = 100
# s.birth = 1993
#
# print(s.age)

'Task 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution'


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be integer")
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024*768=%d' % s.resolution
