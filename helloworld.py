#print:
# a = -111
# if a >= 0:
#     print(a)
# else:
#     print(-a)
#
# a = "abc"
# b = a
# a = "XYZ"
# print(b)

# print("包括中文的编码")
# print()

# print('\u4e2d\u6587')

# print("hello, %s" % "world")

# 字符串占位符
# r = 72 /85 * 100
# print("小明成绩提升的百分点 %.1f %%" % (r))

#list list是一种有序的集合，可以随时添加和删除其中的元素
# classmates = ["lan","xia","an","chen"]
# print(classmates)  # lan,xia,an,chen
# #得到list 长度 用len()函数可以获得list元素的个数
# print(len(classmates)) #4
# #用索引来访问list中每一个位置的元素
# print("%s是帅哥" % (classmates[0])) # lan是帅哥
# #如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
# print("%s is last element" % (classmates[-1])) # chen is last element
#list是一个可变的有序表，所以，可以往list中追加元素到末尾 append()
# classmates.append("admin")
# print(classmates) #"lan","xia","an","chen","admin"
# #也可以把元素插入到指定的位置，比如索引号为1的位置
# classmates.insert(0,"zhang")
# print(classmates) #"zhang","lan","xia","an","chen","admin"
# #要删除list末尾的元素，用pop()方法
# classmates.pop()
# print(classmates) #"zhang","lan","xia","an","chen"
# #要删除指定位置的元素，用pop(i)方法，其中i是索引位置
# classmates.pop(1)
# print(classmates) #"zhang","xia","an","chen","admin"
# #要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
# classmates[1] = "chenshi2"
# print(classmates) #"zhang","chenshi2","an","chen","admin"
# #list里面的元素的数据类型也可以不同，比如
# L = ["name",1,True]
# print(L)
# S =[".NET","JAVA","JavaScript",["Swift,iOS,MacOS"]]
# print(S) #".NET","JAVA","JavaScript",["Swift,iOS,MacOS"]

# -*- coding: utf-8 -*-
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# for name in L:
#     print(name)
#
# list = list(range(100))
# print(list)
#
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# for languages in L:
#     for language in languages:
#         print("hello , %s" % language)
#
# d = {"michael":85,"bob":75,"tracy":85}
# d["chen"] = 85
# print(d["chen"])

# 打印Apple:
# print(L[0][0])
# 打印Python:
# print(L[1][1])
# 打印Lisa:
# print(L[-1][-1])

# height = 1.75
# weight = 80.5
# bmi = weight / (height * height)
# if bmi < 18.5:
#     print("过轻")
# elif 18.5 <=bmi <25:
#     print("normal")
# elif 25 <= bmi <28:
#     print("a little hat")
# elif 28 <= bmi <32:
#     print("	fat")
# else:
#     print("vert fat")

# a = "abc";
# a.replace("a","A")
# print(a);
# n1 = 255
# n2 = 1000
# print(hex(n1),hex(n2))

# def sum(n1,n2):
#     if not isinstance(n1,(int,float)) or not isinstance(n2,(int,float)):
#         raise TypeError("bad operad type")
#     return n1 + n2
#
# n1="a"
# n2=2
# print(sum(n1,n2))
#
# import math
# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx,ny
#
# x,y = move(100,100,60,math.pi / 6)
# print(x,y)
# import math
# def quadratic(a,b,c):
#     if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
#         raise TypeError("bad type")
#     m = b*b - 4*a*c
#     n = -b
#     if m>=0:
#         x1 = (-b + math.sqrt(m)) / (2*a)
#         x2 = (-b - math.sqrt(m)) / (2*a)
#     else:
#         raise ArithmeticError("no anwser")
#     return x1,x2
# print(quadratic(2, 3, 1))

# def power(x,n=2):
#     sum = 1
#     while(n>0):
#         n = n - 1
#         sum = sum * x
#     return sum
#
#
# print(power(2))

# def add_end(L=None):
#     if L is None
#         L = []
#     L.append("End")
#     return L
# print(add_end([1,2,3]))
# print(add_end([4,5,6]))
# print(add_end([7,8,9]))
# print(add_end())
# print(add_end())
#
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = n + sum
#     return sum
#
# nums = [1,2,3,4,5]
# print(calc(*nums))

# def person(name,age,*,city,job):
#     print("name:%s, age:%d,other:%s" % (name,age,kw))
# extra = {"city":"beijing","job":"Engineer"}
# person("chenshi2",18,**extra) #name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

# def person(name,age,*,city,job):
#     print(name,age,city,job)
#
# extra = {"city":"beijing","job":"Engineer"}
# person("chenshi2",18,**extra)

#Example
# def function(a,b,c=0,*args,**kw):
#     print("a=%s,b=%s,c=%d,args=%s,kw=%s" % (a,b,c,args,kw))
#
# def function1(a,b,c=0,*,d,**kw):
#     print("a=%s,b=%s,c=%d,args=%s,kw=%s" % (a,b,c,d,kw))
#
# nums = [1,2,3,4,5]
# extra = {"city":"beijing","job":"Engineer"}
# # function("a","b",2,*nums,**extra)
#
# function(1,2)
# function(1,2,3)
# function(1,2,3,"a","b")
# function(1,2,3,"a","b",x=99)
#
# args =(1,2,3)
# kw = {"d":99,"x":"#"}
# function1(*args,**kw)
#
# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)
#
# print(fact(10))
#
# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
#
# print(fact(10))
#
# def move(n,a,b,c):
#     if n==1:
#         print( a,"-->",c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# num = input("please enter the number :")
# move(int(num),"a","b","c")

# print(list(range(1,50,2)))

# L=["chenshi2","zhangtao1","liuhx06","Jack","Marry"]
# L = list(range(1,100))
# print(L)
# print(L[0:2]) #[1,2]
# print(L[-10:]) #[91,92,93,94,95,96,97,98,99,100]
# print(L[10:20]) #[11,11,12,13,14,15,16,17,18,19,20]
# print(L[0:10:2]) #[1,3,5,7,9]
# print(L[::20]) #[1,21,41,61,81]
# print(L[:]) #原样复制

# str = "ABCDEFG"
# startIndex = 0
# lastIndex = 3
# m = str[startIndex:lastIndex]
# print(m)

# from collections import Iterable

# print(isinstance(123,Iterable))

# for i,value in enumerate(["A","B","C"]):
#     print(i,value)

# for x,y in [(1,1),(2,2),(3,3)]:
#     print(x,y)
#
# L=list(x*x for x in range(1,11))
# print(L)
#
# L = list(x * x for x in range(1,11) if x%2==0)
# print(L)
# #
# M = list(m + n for m in "ABC" for n in "XYZ")
# print(M)
#
# import os
# O = list(d for d in os.listdir("."))
# print(O)
#
# Dict = {"a":1,"b":2,"c":3}
# for k,v in Dict.items():
#     print(k,"=",v)

# for k,v in Dict.items():
#     print(k)
# print(L)

# L = ['Hello', 'World', 18, 'Apple', None]
# L1= [s.lower() for s in L if isinstance(s,(str))]
# print(L1)

#生成器
# L = (x*x for x in range(10))
# for n in L:
#     print(n)

# def fib():
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n +1
#     return "done"
# f = fib(5)
# print(f)
#
# while True:
#     try:
#         x=next(f)
#         print("f",x)
#     except StopIteration as e:
#         print("Generator return value:",e.value)
#         break

# def odd():
#     print("step 1")
#     yield 1
#     print("step 2")
#     yield 3
#     print("step 3")
#     yield 5
#
# o = odd()
# next(o)

# M =[1]
# M.append(0)
# print(M)
# for i in range(len(M)):
#     print(i)
# M1= M[-1] + M[1]
# print(M[-1])

# N = [1]
# N.append(0)
# N = [N[i - 1] + N[i] for i in range(len(N))]
#
# print(N)

# from collections import Iterable
# print(isinstance((x for x in range(10)), Iterable))  #True
# print(isinstance([], Iterable))  #True
# print(isinstance({}, Iterable))  #True
# print(isinstance("abc", Iterable))  #True
# print(isinstance(100, Iterable))  #False
#
# from collections import Iterator
# print(isinstance((x for x in range(10)), Iterator))  #True
# print(isinstance([], Iterator))  #False
# print(isinstance({}, Iterator))  #False
# print(isinstance("abc", Iterator))  #False
# print(isinstance(100, Iterator))  #False
# def triangles():

# for x in [1,2,3,4,5]:
#     print(x)
#
# it = iter([1,2,3,4,5])
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration as e:
#         break;

# from math import sqrt

# def add(x, y, *fun):
#     return (m(x) + m(y) for m in fun)
# def getAbs(val):
#     return abs(val)
#
#
# print(add(1, -22, abs,sqrt))
# O = add(1, 22, abs, sqrt)
# while True:
#     try:
#         x = next(O)
#         print(x)
#     except StopIteration as e:
#         print("done")
#         break

# def f(n):
#     return n * n

# r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))

from functools import reduce

#
# def add(x, y):
#     return x * 10 + y

# O = map(char2num,['1','2','3','4','5','6'])
# while True:
#     try:
#         x = next(O)
#         print(x)
#     except StopIteration as e:
#         break
#         print("done")

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def char2num(s):
#
#         return {"0": 0,
#                 "1": 1,
#                 "2": 2,
#                 "3": 3,
#                 "4": 4,
#                 "5": 5,
#                 "6": 6,
#                 "7": 7,
#                 "8": 8,
#                 "9": 9}[s]
#
#     return reduce(fn, (map(char2num, s)))
# print(map(char2num,[1,2,3,4,5,6]))
# print(str2int(["1", "2", "3", "4", "5"]))

################################################
# def normalize(name):
#     return name.capitalize()
#
#
# L1 = ['adam', 'LISA', 'barT']
# print(list(map(normalize, L1)))

###################################################

#
# def char2num(s):
#     return {"0": 0,
#             "1": 1,
#             "2": 2,
#             "3": 3,
#             "4": 4,
#             "5": 5,
#             "6": 6,
#             "7": 7,
#             "8": 8,
#             "9": 9}[s]
#
#
# def prod(L):
#     return reduce(lambda x, y: x * y, map(char2num, L))
#
#
# print("3 * 5 * 7 * 9 =", prod(["3", "5", "7", "9"]))
# ##################################################
#
# def str2float():
#     i = input(">>>>")
#     sint = i.split(".")
#     if i.find(".") == -1:
#         return reduce(lambda x,y:x*10+y,map(char2num,i))
#     else:
#         a = reduce(lambda x,y:x*10+y,map(char2num,sint[0]))
#         b = reduce(lambda x,y:x*10+y,map(char2num,sint[1]))*0.1**len(sint[1])
#         return a+b
#
# print(str2float())
#
# print(**len(2))

#     N=[1]
#     while True:
#         yield N
#         print(N)
#         N.append(0)
#         N = [N[i-1] + N[i] for i in range(len(N))]
#
# n=0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if(n==2):
#         break

# L = [1, 2, 3, 4, 5, 6, 7, 81, 55, 77]
#
#
# def is_odd(n):
#     return n % 2 == 0
#
#
# def not_empty(s):
#     return isinstance(s, str) and s and s.strip()
#
#
# L1 = list(filter(is_odd, L))
# print(L1)
#
# strList = ["A", "B", "C", "D", None, "", 123]
# print(list(filter(not_empty, strList)))
#
#
# #生成3的序列基数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

#定义筛选器
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()  #初始化序列
#     while True:
#         n = next(it)  #返回序列的第一个参数
#         yield n
#         it = filter(_not_divisible(n), it)  #构造新序列
#
#
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# L = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# L1 = L[::]
# L2 = L[::-1]
# print(L1, "---", L2)

#
# def is_palindrome(n):
#     n = str(n)
#     # i=0
#     # while str(n)[i]==str(n)[-i-1]:
#     #     return n
#     #     i = i +1
#     return n[::] == n[::-1]
#
#
# print(list(filter(is_palindrome, range(1, 10000))))

#sorted

# L = [36, 5, -2, -56, -12, 44]
# strlist = [("bob", 88), ("About", 99), ("Zoo", 100), ("Credit", 55)]
#
# print(sorted(strlist, key=lambda m: m[1], reverse=True))

# def calc_sum(*args):
#     ax= 0
#     for n in args:
#         ax = ax +n
#     return ax

#闭包
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1,2,3,45,6)
# print(f())

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

# print(list(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
import functools


# def log(func):
#     def wrapper(*args, **kw):
#         print("call %s():" % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
def log(text):
    def decorator(func=text):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call %s()" % func.__name__)
            return func(*args, **kw), print("%s %s()" %
                                            ("end call", func.__name__))

        return wrapper

    return decorator


def f2():
    @log
    def now():
        print("2015-02-23")


f2()
# print(now.__name__)

####################
# def log(*text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*arg, **kw):
#             print("%s %s()" % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print("%s %s():" % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
# @log("excute")
# def now():
#     print("2015-02-23")
#
# print(now.__name__)
