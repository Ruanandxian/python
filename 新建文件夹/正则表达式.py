import re
test=r'^\d{3}\-\d{3,8}$'
if re.match(test,'111-545455'):
    print('ok')
else:
    print('failed')

print(re.split(r'[\s\,]+','1 ,, 2   5 8 5'))

m=re.match(r'^(\d{3})-(\d{3,8})$','110-123154')
print(m)
print(m.group(1))
print(m.group(2))


print(re.match(r'(\d+?)(0*)$','102300').groups())#默认贪婪匹配，加？非贪婪匹配