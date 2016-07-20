'判断基本数据类型'


def get_type(args):
    print(type(args))


get_type("1234")
get_type(1234)
get_type(None)
get_type(abs)
# get_type(dog)

'判断是否为函数'
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(1, 10))) == types.GeneratorType)

'判断class 类型,可以使用isinstance 函数'
#并且还可以判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))

print('ABC'.__len__())

print(hasattr('abc', '__len__'))


