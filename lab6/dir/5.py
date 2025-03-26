import os

path = "."
isExist = os.access(path,os.F_OK)
if not isExist:
    print("Current directory doesn't exist")
else:
    list = ["I'm", "tireddddd"]
    with open("file2.txt","w") as file:
        for i in list:
            file.write(i+"\n")