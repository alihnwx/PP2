with open("file2.txt","r") as file:
    content = file.read()
    print(content)
with open("copy.txt","w") as file:
    file.write(content)