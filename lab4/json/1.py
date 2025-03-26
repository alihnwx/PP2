import json

# Читаем JSON-файл
with open("sample-data.json") as file:
    data = json.load(file)

# Заголовки
print("Interface      | Admin State | MTU  | Description")
print("-" * 50)

# Извлекаем и выводим данные
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    print(f"{attributes['id']:14} | {attributes['adminSt']:10} | {attributes['mtu']:4} | {attributes['descr']}")