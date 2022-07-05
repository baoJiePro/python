school = "old"


def fun1():
    global school
    school = "new"


fun1()

print(school)


def calc(n):
    print(n)
    if int(n / 2) > 0:
        return calc(int(n / 2))
    print("--->", n)


calc(10)
