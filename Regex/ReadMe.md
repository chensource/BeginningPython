#正则表达式


###如果正则表达式匹配成功,返回一个`Match`对象, 失败了返回`None`

```python
test = '用户输入的字符串'
	if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
```

###如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配
``` python
import re
# 编译:
>>>re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>>re_telephone.match('010-12345').groups()
('010', '12345')
>>>re_telephone.match('010-8086').groups()
('010', '8086')
```
