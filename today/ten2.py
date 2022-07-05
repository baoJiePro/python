# ### 文件操作
'''
fp = open("打开的文件",mode="模式选择",encoding="编码集")
open 函数 返回一个文件io对象 (别名:文件句柄)
i => input   输入
o => output  输出
'''

"""
把大象放冰箱里:需要三部
	打开冰箱门
	把大象塞进去
	关上冰箱门
"""

# (1)写入文件内容
# 打开文件
fp = open("0414.txt", mode="w", encoding="utf-8")
fp.write("我就是那个大象")
fp.close()

fp = open("0414.txt", mode="r", encoding="utf-8")
res = fp.read()
fp.close()
print(res)
