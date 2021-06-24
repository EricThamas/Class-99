import shutil
import os
# path="/Users/Eric/OneDrive/Desktop/Files and videos"
# print(os.listdir(path))
# source="/Users/Eric/OneDrive/Desktop/Files and videos/mylivewallpapers.com-Lo-Fi-Girl.mp4"
# destination="/Users/Eric/OneDrive/Desktop/New/mylivewallpapers.com-Lo-Fi-Girl.mp4"
# copy=shutil.copy(source,destination)

path="/Users/Eric/OneDrive/Desktop/Files and videos"
print(os.listdir(path))
#"C:\Users\Eric\OneDrive\Desktop\Files and videos\buzzer.png"
#"C:\Users\Eric\OneDrive\Desktop\Files and videos\buzzer.png"
source="/Users/Eric/OneDrive/Desktop/Files and videos/buzzer.png"
destination="/Users/Eric/OneDrive/Desktop/New/buzzer.png"
copy=shutil.move(source,destination)

