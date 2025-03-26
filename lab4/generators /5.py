def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Тестирование генератора
for num in countdown(5):
    print(num)