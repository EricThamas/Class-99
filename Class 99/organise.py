# import os
# import shutil
# path=input("enter the file name to organise")
# list_of_files=os.listdir(path)

# for file in list_of_files:
#     name,ext= os.path.splitext(file)
#     ext=ext[1:]
#     if ext== " ":
#         continue
#     if os.path.exists(path+ "/"+ ext ):
#       shutil.move(path+ "/" + file, path+ "/" + ext + "/" + file)
#     else:
#       os.makedirs(path+ "/" + ext)
#       shutil.move(path+ "/" + file,path+ "/" + ext + "/" + file)

import shutil 
import os 
path = input("enter the file name to orgainse") 
list_of_files = os.listdir(path)

for file in list_of_files: 
    
    name,ext = os.path.splitext(file) 
    ext = ext[1:]
    if ext == "": 
        continue 
    if os.path.exists(path + "/" + ext): 
        shutil.move(path + "/" + file,path + "/" + ext + "/" + file) 
    else: 
        os.makedirs(path + "/" + ext) 
        shutil.move(path + "/" + file,path + "/" + ext + "/" + file)
