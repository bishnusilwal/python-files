name1={'ram','sohail','bishnu','hari'}
name2={'ram','sita','bishnu','geeta'}
name3={'krishna','ram','sita','bishnu'}
a=(name1.intersection(name2,name3))
b=(name1.difference(name2,name3))
c=(name1.union(name2,name3))
d=(c.difference ,a)

print('reapeated items'(a))
print('unique items',d)
print('unrepeated items',c)


