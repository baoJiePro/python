
import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))

# 将字典序列化成json字符串
j = json.dumps(dic)
print(type(j))
print(j)

f = open('序列化对象', 'w')
# f.write(j)
json.dump(dic, f)
f.close()


fr= open('序列化对象', 'r')
# data = json.loads(f.read())
data = json.load(fr)

print(data['name'])
fr.close()


# 将json字符串转换成字典或其他
data2 = json.loads(j)

print(data2['age'])


