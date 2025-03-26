try:
    with open("file.txt","r") as file:
        lines = file.readlines()
        print(lines)
        print(len(lines))
except:
    print("Nothing")