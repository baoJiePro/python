class Dog(object):
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print("%s 调用了bulk" %self.name)



choice = input(">>:").strip()

d1 = Dog('andy')

if hasattr(d1, choice):
    getattr(d1, choice)()

