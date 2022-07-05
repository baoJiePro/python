import hashlib

m = hashlib.md5()

m.update("hello哈哈".encode(encoding='utf-8'))

print(m.hexdigest())