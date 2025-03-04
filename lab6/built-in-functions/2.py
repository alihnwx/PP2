def count_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Пример
text = "Hello World!"
print(count_letters(text))  # Вывод: (2, 8)