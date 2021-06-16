# coding: utf-8

import os
import shutil

print(os.getcwd())

root_path='./data/dogs'

train='./data/train/dogs'
test='./data/test/dogs'

# 创建目录
if not os.path.exists(train):
    os.makedirs(train) # mkdir 创建指定路径目录, makedirs 创建父、子目录
if not os.path.exists(test):
    os.makedirs(test)

files=os.listdir(root_path) # 列出目录下的所有文件, list[str1, str2, str3]
for file in files[:5]: # 列表切片 1-5
    filepath=root_path+'/'+file
    shutil.copy(filepath,train) # 复制文件
for file in files[5:]: # # 列表切片 1-5
    filepath=root_path+'/'+file
    shutil.copy(filepath,test)  

with open('./Q1.txt','w') as f: # w 写 r 读 '+' 追加
    for file in files:
        f.write(file+'\n')
    f.close()