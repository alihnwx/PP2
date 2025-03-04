import os

put = r"/Users/alihaan/Desktop/PP2/lab6/dir"

isExist = os.path.exists(put)
print(f'"Path {put} is {isExist}')
if isExist:
    print(f"PathName: {os.path.dirname(put)}")
    print(f"DirName: {os.path.basename(put)}")