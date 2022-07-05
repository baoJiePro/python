""" list 可获取,可修改,有序"""
listvar = []
print(listvar, type(listvar))

listvar = [13, 3.14, True, 6 - 2j, "我是大帅哥"]
res = listvar[4]
res = listvar[-1]
print(res)

res = len(listvar) - 1
print(listvar[res])
listvar[3] = "和抚慰"
print(listvar)

""" tuple 可获取,不可修改,有序"""

turtlevar = ()
turtlevar = (1, 2, 3)
tuplevar = 1, 2, 3
print(turtlevar, type(tuplevar))

# ### set 集合 (用来做交叉并补 集合操作的)
'''自动去重 无序'''
setvar = {"周杰伦", "王宝强", "李宇春"}
print(setvar, type(setvar))

setvar = {"刘德华", "张学友", "郭富城", "王文", "王文"}
print(setvar)

# ### dict 字典
"""
# 关于字典 
在3.6版本之前,字典无序,
在3.6版本之后,字典有序(看起来有序,本质上无序)

哈希算法:
	将不可变的任意长度值计算成具有固定长度的唯一值,
	这个值可正可负,可大可小,通过计算出来的键,来获取值,形成一一映射的效果
	管这个算法叫哈希算法,这个值叫哈希值

	字典进行存储的时候,并不一定按照字面顺序依次存在内存中
	而是通过哈希算法,随机散列的把键所对应的值存储在内存里,所以字典无序(为了求效率,图快)
	可以通过哈希算出的键获取散列的值

	3.6的之后,记录了字典的字面顺序,在取出数据时,进行重新排序,所以看起来有序(但本质上无序,只要他使用了哈希)

	可哈希数据(不可变的数据) : Number(int float complex bool) str tuple
	不可哈希数据(可变数据)   : list  set  dict  (list dict 值可变 ; set 顺序可变)

	字典的键 集合的值 都需要可哈希数据,剩下的数据无所谓.
"""
'''由键值对数据组成,有序'''

dictvar = {}
print(dictvar, type(dictvar))

dictvar = {"top": "程咬金", "middle": "妖姬", "bottom": "崔丝塔娜", "jungle": "七大大声", "support": "德玛西亚"}
print(dictvar, type(dictvar))

# 获取字典当中的值 (通过键来获取值)
res = dictvar['middle']
print(res)

# 通过字典的键来修改值
dictvar['top'] = "赵信"
print(dictvar)

# 字典的键唯一  如果两个键相同 后面的覆盖前面的
# 字典的键是唯一不可修改,字典的值随意
dictvar = {"a": 1, 'a': 2}
print(dictvar)
