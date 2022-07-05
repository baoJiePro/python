
import shutil

# shutil.copyfileobj(f1, f2)

shutil.copyfile("os_test.py", "os_test1.py")


import os,sys

current_dir = os.path.abspath(__file__);

path_dir1 = os.path.normpath(current_dir)
print(path_dir1)
path_dir2 = os.path.normpath(os.path.join(current_dir, os.pardir))
print(path_dir2)
path_dir3 = os.path.normpath(os.path.join(current_dir, os.pardir, os.pardir))
print(path_dir3)

sys.path.insert(0, path_dir3)
print(sys.path)