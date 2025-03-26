import os

path = "/Users/alihaan/Desktop/PP2/lab6/dir/test.txt"  

isExist = os.access(path, os.F_OK)

if not isExist:
    print("Файл не существует.")
else:
    print("Файл существует:", isExist)
    print("Читаемый:", os.access(path, os.R_OK))
    print("Записываемый:", os.access(path, os.W_OK))
    print("Исполняемый:", os.access(path, os.X_OK))

    # Удаляем, если доступны все права
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
        print("Файл успешно удалён!")
    else:
        print("Нет достаточных прав для удаления файла.")