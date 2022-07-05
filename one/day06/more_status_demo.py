class Animal(object):
    n = "123"

    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod  # 静态方法跟类没什么关系
    # @classmethod
    def animal_talk(object):
        print("类变量n= %s" % (object.n))
        object.talk()


class Cat(Animal):
    param = "哈哈"

    def talk(self):
        print('%s: 喵喵喵!' % self.name)

    @classmethod
    def eat(self):
        print("吃鱼 %s" % self.param)

    @property
    def param(self):
        print("param")


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):  # 一个接口，多种形态
    obj.talk()


c1 = Cat('小晴')
d1 = Dog('李磊')

func(c1)
func(d1)

Animal.animal_talk(c1)
Animal.animal_talk(d1)

c1.eat()
