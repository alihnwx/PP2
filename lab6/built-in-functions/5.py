def all_true(t):
    return all(t)

# Пример
print(all_true((True, True, 1, "Hello")))  # True
print(all_true((True, False, 1, "Hello")))  # False