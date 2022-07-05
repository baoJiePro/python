
import os
import sys
print(__file__)
print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 项目的目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_PATH)

from core import main

main.main()
