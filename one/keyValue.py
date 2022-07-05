import os

info = {
    'stu1': 'a',
    'stu2': 'b',
    'stu3': 'c',
}

print(info)

print(info['stu1'])

info['stu4'] = 'b'
del info['stu1']

info.pop("stu2")
print(info.get('stu2'))


print(info)
print('stu3' in info)

for i in info:
    print(i, info[i])
