class Dog:
    def __init__(self, name):
        self.name = name

    def bulk(self):
        print('汪汪汪 %s' % self.name)


d1 = Dog('1')
d2 = Dog('2')
d3 = Dog('3')
d4 = Dog('4')

d1.bulk()
d2.bulk()
d3.bulk()
d4.bulk()


