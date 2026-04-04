import os
import shutil

# create nested dirs
os.makedirs("test_dir/sub_dir", exist_ok=True)

# list files
print(os.listdir("."))

# find .txt files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

# move file
shutil.move("demofile.txt", "test_dir/demofile.txt")

# copy back
shutil.copy("test_dir/demofile.txt", "demofile_copy.txt")