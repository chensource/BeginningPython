'私有变量 - 封装'


class Student(object):
    name = 'Student'

    # def __init__(self, name, score):
    #     self.__name = name
    #     self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= self <= 100:
            self.__score = score
        else:
            raise ValueError("Bad Score")

    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            print('%s grade is A' % self.__name)
        elif self.__score >= 60:
            print('%s grade is B' % self.__name)
        else:
            print('%s grade is C' % self.__name)


if __name__ == "__main__":
    pass
    # bart = Student("bart", 59)
    # lisa = Student("Lisa", 87)
    # bart.print_score()
    # lisa.print_score()
    
    # print(bart.get_name())

# s = Student()
# print(Student.name)
# s.name = 'Michael'
# print(s.name)
# print(Student.name)
# del(s.name)
# print(s.name)
