import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Переводим миллисекунды в секунды
    return math.sqrt(number)

# Пример
num = 25100
delay = 2123  # 2123 миллисекунды
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")