import os
import shutil
from unicodedata import name
from_dir="C:/Users/HP/Downloads"
to_dir="D:/org"
list=os.listdir(from_dir)
print(list)
for file in list:
    name,extension=os.path.splitext(file)