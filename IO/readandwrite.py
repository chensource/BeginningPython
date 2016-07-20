'''
读写
'''
# try:
#     f = open('test.txt', 'w')
#     print(f.read())
# finally:
#     f.close()

#等价于上面
# with open('test.txt', 'r') as f:
#     print(f.read())

# with open('test.txt', 'r', encoding='gbk',errors='ignore') as f:
#     print(f.read())
from io import StringIO
# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('world!'))
# print(f.getvalue())

# f1 = StringIO("Hello\nhi\nworld!")
#
# while True:
#     s = f1.readline()
#     if s == '':
#         break
#     print(s.strip())

import os

# print(os.uname)

# print(os.environ.get('PATH'))

#查看当前文档的绝对路径
# print(os.path.abspath('.'))

# d = os.path.abspath('.')
# dirName = 'testdir'
# newpath = os.path.join(d, dirName)

#文件名称
# print(os.path.split(newpath))

# a = [x for x in os.listdir('.')
#      if os.path.isdir(x) or os.path.splitext(x)[1] == '.py']
# print(a)

# os.mkdir(newpath)

# def dir_l(path='.'):
#     L = os.listdir(os.path.abspath(path))
#     for file in L:
#         print(file)
#
#
# dir_l()
#
#
# def findfile(findName):
#     #当前目录的绝对路径
#     dirlist = os.walk(os.path.abspath('.'))
#     print(dirlist)
#     result = list()
#
#     for root, dirs, files in dirlist:
#         for file in files:
#             if findName in file and findName != '':
#                 print('包含\'%s\'的文件路径为:' % findName, os.path.join(root, file))
#                 result.append(os.path.join(root, file))
#
#     if len(result) == 0:
#         print('没有找到包含\'%s\'的文件' % findName)
#
#
# findfile('')

import pickle
import json
from PIL import Image

# d = dict(name="bob", age=20, score=88)
# pickle.dumps(d)
# print(d)

# with open("test.txt",
#           mode='wb',
#           buffering=-1,
#           encoding=None,
#           errors=None,
#           newline=None,
#           closefd=True) as f:
#     pickle.dump(d, f)

# with open('test.txt', mode='rb', closefd=True) as f:
#     d = pickle.load(f)
#     print(d)

# d = dict(name="bob", age=20, score=88)
# jsonStr = "{'name': 'bob', 'age': 20, 'score': 88}"
# json.loads(jsonStr)

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score

# def student2dict(std):
#     return {'name': std.name, 'age': std.age, 'score': std.score}
#
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
#
# s = Student('bob', 20, 94)
# print(json.dumps(s, default=lambda obj: obj.__dict__))
#
# json_str = '{"name": "bob", "age": 20, "score": 94}'
# print(json.loads(json_str, object_hook=dict2student))


class Goods(object):
    def __init__(self, goodsID, classID, goodsName, goodsListImg):
        self.goodsID = goodsID
        self.classID = classID
        self.goodsName = goodsName
        self.goodsListImg = goodsListImg


def dict2Goods(d):
    return Goods(d['goodsID'], d['classID'], d['goodsName'], d['goodsListImg'])


L = []
with open('test.txt', 'r') as f:
    for d in json.load(f, object_hook=dict2Goods):
        L.append(d)

for i in L:
    im = Image.open(i.goodsListImg)
    print(im.format, im.size, im.mode)
    # PNG(400,300) RGB
    im.thumbnail((200, 100))
    im.save(L.index, "JPEG")
    # print(i.goodsListImg)
