import keyword

res = keyword.kwlist
print(res)

a = 11
b = 12
a, b = b, a
print(a, b)

print(type(a))
print(id(a))

intvar = 0b101
print(intvar)
print(type(intvar))
print(id(intvar))
print("=================")

floatvar = 3.15
print(floatvar, type(floatvar))

complexvar = complex(-5, -2)
print(complexvar, type(complexvar))

print("==================")

strvar = '我爱你亲爱的菇凉'
print(strvar, type(strvar))

strvar = r"黑夜给我了黑色的眼睛,\r但是我却用它翻白眼"
strvar = r"C:\Windows\System32\drivers\etc"
print(strvar)

strvar = "肖成勇,一个月%.2f元,买了%d个娃娃,感觉身体%s" % (999.987, 10, "被榨干")
print(strvar)
