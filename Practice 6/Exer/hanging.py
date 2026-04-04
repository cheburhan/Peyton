import shutil
import os

# read and print
with open("demofile.txt", "r") as f:
    print(f.read())

# append
with open("demofile.txt", "a") as f:
    f.write("\nNew line added")

with open("demofile.txt", "r") as f:
    print(f.read())

# copy / backup
shutil.copy("demofile.txt", "demofile_backup.txt")

# safe delete
if os.path.exists("demofile_backup.txt"):
    os.remove("demofile_backup.txt")