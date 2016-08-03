import itertools

for c in itertools.chain('abc','xyz'):
    print(c)

for key,group in itertools.groupby('AAAABBBDEFFAAADDCDR'):
    print(key,list(group))
