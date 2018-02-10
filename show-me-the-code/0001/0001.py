#!/user/bin/env
'''
Self-defined activation code
1. has length of 10
2. mixture of letters and numbers
3. unique throughtout 200 combos
Pros:
total of 3656158440062976 combos, randomly generation of 200 is almost
guaranteed to be unique; Confident level if high without look up opeations.
And without look up, it's super fast :) The more codes needed, the effect
is more obvious.
Cons:
Without back tracking, small chance would occur of duplication.
'''

'''
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import random

codeSeedA = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def digit(raw):
    l = len(raw)
    # randrange() 是关于生产平均分配值更复杂 . int(random()*n) 这可能会产生轻微的不均匀分布。
    return raw[random.randrange(l)]


def codeGen(n):
    codes_pool = []
    for i in range(n):
        code = ""
        for i in range(10):
            code += digit(codeSeedA)
        codes_pool.append(code)
    return codes_pool


'''
Standard uuid
'''
import uuid


def uuidGen(n):
    codes_pool = []
    for i in range(n):
        codes_pool.append(uuid.uuid4())
    return codes_pool

codes_udf = codeGen(20000)
# codes_uuid = uuidGen(20000)

for i in codes_udf:
    print(i)
