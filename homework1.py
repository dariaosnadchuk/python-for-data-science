import random

# 1. Створюємо двовимірний масив 3x3 з випадкових чисел від 1 до 100
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Початковий масив:")
for row in matrix:
    print(row)
print("-" * 30)

# 2. Обчислюємо суму всіх елементів масиву
total_sum = sum(sum(row) for row in matrix)
print(f"Сума всіх елементів: {total_sum}")
print("-" * 30)

# 3. Знаходимо макс/мін значення та їхні індекси
# Ініціалізуємо початковими значеннями з першого елемента [0][0]
min_val = max_val = matrix[0][0]
min_idx = max_idx = (0, 0)

for r in range(3):
    for c in range(3):
        current_value = matrix[r][c]

        # Перевірка на мінімум
        if current_value < min_val:
            min_val = current_value
            min_idx = (r, c)

        # Перевірка на максимум
        if current_value > max_val:
            max_val = current_value
            max_idx = (r, c)

print(f"Мінімальне значення: {min_val} (Індекс: ряд {min_idx[0]}, стовпець {min_idx[1]})")
print(f"Максимальне значення: {max_val} (Індекс: ряд {max_idx[0]}, стовпець {max_idx[1]})")
print("-" * 30)

# 4. Сортуємо масив по кожному рядку
for row in matrix:
    row.sort()

print("Відсортований масив (по рядках):")
for row in matrix:
    print(row)

# dev