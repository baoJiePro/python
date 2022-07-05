import sys
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # sys.stdout.write(str(b))
        # sys.stdout.write(",")
        # print(b)
        a, b = b, a + b
        n = n + 1
    return 'done' # next调用多了出错的时候打印


print(fib(25))
f = fib(25) 

print(f.__next__())
print(f.__next__())
print("=======")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())



print("====start")
for i in f:
    print(i)

g = fib(4)

while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("generator return value:", e.value)
        break