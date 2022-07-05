class Role(object):
    n = 123
    name = "类name"

    # 构造函数，在实例化做一些初始化的工作
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))

    def __del__(self):
        # 实例释放后调用
        print("结束了")


r1 = Role('Alex', 'police', 'AK47')
r2 = Role('Jack', 'terrorist', 'B22')

r1.got_shot()
r1.buy_gun('B51')
print(r1.name)
print(Role.n)
print(Role.name)
