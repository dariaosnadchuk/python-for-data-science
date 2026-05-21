import numpy as np

# 1. Створюємо одновимірний масив з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, size=200)

print("Початковий масив (перші 20 елементів для наочності):")
print(array[:20])
print("-" * 40)

# 2. Використовуючи маску, відфільтровуємо всі додатні числа (> 0)
positive_mask = array > 0
positive_numbers = array[positive_mask]

print("Тільки додатні числа (перші 20 елементів):")
print(positive_numbers[:20])
print("-" * 40)

# 3. Замінюємо всі від’ємні значення (< 0) на нулі
# Створюємо маску для від'ємних чисел і відразу перезаписуємо їх
negative_mask = array < 0
array[negative_mask] = 0

print("Масив після заміни від'ємних чисел на нулі (перші 20 елементів):")
print(array[:20])
print("-" * 40)

# 4. Обчислюємо середнє значення отриманого масиву
average_value = np.mean(array)
print(f"Середнє значення отриманого масиву: {average_value:.2f}")