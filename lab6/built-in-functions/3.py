def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]

# Пример
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False