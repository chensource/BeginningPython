import re

# pattern = r'^\d{3}-\d{3,8}$'
# result = re.match(pattern, '010-12345')
# print(result)
# result.group[0]
#
# #正则表达式切割字符
# L = re.split(r'[\s\,]+', 'a bc,c,c cd  d lf')
#
# print(L)
pattern = r'^(\d{3})-(\d{3,8})$'
m = re.match(pattern, '010-12345')
print(m)
print(m.group(0))


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').group(2))
