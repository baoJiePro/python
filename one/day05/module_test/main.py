import module_text
from module_text import say_baybay as say

# 导入所有
# from module_text import *

print(module_text.name)
# print(name)

module_text.say_hello()
# say_hello()

module_text.say_baybay()

say()

import os,sys

print(sys.path)

p1 = os.path.abspath(__file__)
print(p1)
p2 = os.path.dirname(p1)
print(p2)
p3 = os.path.dirname(p2)
print(p3)

sys.path.append(p3)
# sys.path.insert(p3)
print(sys.path)
import package_test

package_test.pa_test.say_pa()




