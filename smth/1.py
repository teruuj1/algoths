import numpy as np
import matplotlib.pyplot as plt
import random


def find_max_with_counter(arr):
    """Находит максимальный элемент и подсчитывает присваивания"""
    if not arr:
        return None, 0

    max_val = arr[0]
    assignments = 1  # первое присваивание max_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            assignments += 1  # счетчик увеличивается при каждом присваивании

    return max_val, assignments


# Параметры эксперимента
n = 1000000
num_experiments = 50

# Аккуратная генерация случайных массивов
random.seed(42)  # для воспроизводимости
np.random.seed(42)

assignments_count = []

print("Проведение экспериментов...")
for exp in range(num_experiments):
    # Генерация случайного массива
    arr = [random.randint(1, 1000000) for _ in range(n)]

    # Находим максимум и считаем присваивания
    max_val, assignments = find_max_with_counter(arr)
    assignments_count.append(assignments)

    if (exp + 1) % 10 == 0:
        print(f"Завершен эксперимент {exp + 1}/{num_experiments}")

# Статистика
mean_assignments = np.mean(assignments_count)
std_assignments = np.std(assignments_count)

print(f"\nРезультаты ({num_experiments} экспериментов):")
print(f"Среднее количество присваиваний: {mean_assignments:.2f}")
print(f"Стандартное отклонение: {std_assignments:.2f}")
print(f"Минимальное количество: {min(assignments_count)}")
print(f"Максимальное количество: {max(assignments_count)}")

# Теоретическая оценка (H_n - гармонический ряд)
# Ожидаемое количество присваиваний ≈ H_n = 1 + 1/2 + 1/3 + ... + 1/n
H_n = sum(1 / i for i in range(1, n + 1)) if n <= 10000 else 14.392726  # приближение для больших n
print(f"Теоретическая оценка (H_n): {H_n:.2f}")

# Построение гистограммы
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(assignments_count, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(mean_assignments, color='red', linestyle='--', linewidth=2, label=f'Среднее: {mean_assignments:.2f}')
plt.xlabel('Количество присваиваний')
plt.ylabel('Частота')
plt.title('Гистограмма количества присваиваний')
plt.legend()
plt.grid(True, alpha=0.3)

# График всех экспериментов
plt.subplot(1, 2, 2)
plt.plot(range(1, num_experiments + 1), assignments_count, 'bo-', alpha=0.7, markersize=4)
plt.axhline(mean_assignments, color='red', linestyle='--', linewidth=2, label=f'Среднее: {mean_assignments:.2f}')
plt.xlabel('Номер эксперимента')
plt.ylabel('Количество присваиваний')
plt.title('Количество присваиваний по экспериментам')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()