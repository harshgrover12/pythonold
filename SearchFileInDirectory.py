import os, glob

print(os.getcwd())
for file in glob.glob("*.png"):
    print(file)  # python1.png
