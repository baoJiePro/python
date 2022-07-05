
import json
import pickle

info = {
    "name": "bj",
    "age": 23
}

f = open("b.txt", "wb")

# f.write(json.dumps(info))
# 序列化出来的是二进制
# f.write(pickle.dumps(info))
pickle.dump(info, f)
f.close()

fi = open("b.txt", "rb")

# data = json.loads(fi.read())
# data = pickle.loads(fi.read())
data = pickle.load(fi)
print(data["name"])

