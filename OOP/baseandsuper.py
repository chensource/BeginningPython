class Animal(object):
    def run(self):
        print("Animal is Running...")


class Dog(Animal):
    def run(self):
        print("Dog is Running...")

    def eat(self):
        print("Eating meat...")


class Cat(Animal):
    def run(self):
        print("Cat is Running...")


def run_twice(Animal):
    Animal.run()
    Animal.run()

    # dog = Dog()
    # dog.run()


class Timer(object):
    def run(self):
        print("start....")

# a = list()
# b = Animal()
# c = Dog()
#
# print(isinstance(a, list))
# print(isinstance(b, Animal))
# print(isinstance(c, Dog))
# print(isinstance(c, Animal))
# print(isinstance(b, Dog))

# run_twice(Timer())

# from demo import Student
#
# s = Student()
# print(s.name)

import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
