res = 14 // 7
print(res)

strvar = "如果遇到你是一种错,那我宁愿一错再错"
res = "你" in strvar
res = "遇到" in strvar
res = "那宁" in strvar
print(res)

listvar = ["钟立文", "刘鹏", "何伟福", "龙阳"]
res = "龙阳" not in listvar
print(res)

setvar = {"戴明雪", "郑慢", "林志元", "中灵芝"}
print(setvar)
res = "郑慢" in setvar
print(res)

tuplevar = ("胡家豪", "徐欣欣", "胡斌")
res = "徐欣欣" not in tuplevar
print(res)

# dict  成员运算符 判断字典时 判断的是键 不是那个所对应的值
dictvar = {"top": "程咬金", "bottom": "甄姬", "middle": "嫦娥"}
res = "程咬金" in dictvar
res = "top" not in dictvar
print(res)

var1 = 19
var2 = 19
res = var1 is var2
print(res)

var1 = -5.52
var2 = -5.52
res = var1 is not var2
print(res)

var1 = 3 + 4j
var2 = 3 + 4j
res = var1 is var2
print(res)

var1 = True
var2 = True
res = var1 is var2
print(res)

var1 = "你"
var2 = "你"
print(var1 is var2)

var1 = (1, 23)
var2 = (1, 23)
print(var1 is var2)

var1 = [1, 2]
var2 = [1, 2]
print(var1 is not var2)

# ### 逻辑运算符 and or not
print("<============>")

res = True and True
res = True and False
res = True or False
print(res)

res = not True
res = not False
print(res)

res = 5 or 6 and 7
res = (5 or 6) and 7
res = not (5 or 6) and 7
print(res)

intVar = 15
print(isinstance(intVar, int))
strvar = "789"
print(isinstance(strvar, (int, str, list)))
