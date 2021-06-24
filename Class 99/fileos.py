import os
#os.system("date")
# cws=os.getcwd()
# print("check the current path:",cws)
# C:\Users\Eric\OneDrive\Desktop\Class 99
#os.mkdir("/Users/Eric/OneDrive/Desktop/New")

# path="/Users/Eric/OneDrive/Desktop/New"
# check=os.path.exists(path)
# print(check)

path="/Users/Eric/OneDrive/Desktop/purple.jpg"
root=os.path.splitext(path)
print(root[1])