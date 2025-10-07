import numpy as np
import matplotlib.pyplot as plt

def harmonic_series_lower_bound(n):
    """Строит оценку снизу для гармонического ряда"""

    # Точное вычисление для небольших n
    if n <= 100000:
        exact_sum = sum(1 / i for i in range(1, n + 1))
    else:
        # Приближение для больших n
        exact_sum = None

    # Оценка снизу через интеграл
    # интеграл от (1/x)dx от 1 до n+1 = ln(n+1) < H_n
    # Но нам нужна оценка СНИЗУ: H_n > ln(n+1)

    # Более точная оценка снизу: H_n > ln(n) + 1/(2n) + γ
    # где γ примерно равно 0.57721 - постоянная Эйлера-Маскерони

    gamma = 0.57721566490153286060651209  # постоянная Эйлера

    # Несколько оценок снизу:
    lower_bounds = {
        "ln(n) + γ": np.log(n) + gamma,
        "ln(n+1)": np.log(n + 1),
        "ln(n) + 1/(2n) + γ": np.log(n) + 1 / (2 * n) + gamma,
        "ln(n) + 1/(2n) + 1/(12n²) + γ": np.log(n) + 1 / (2 * n) + 1 / (12 * n ** 2) + gamma
    }

    print(f"Оценки снизу для гармонического ряда H_{n}:")
    print("=" * 50)

    for name, bound in lower_bounds.items():
        print(f"{name:30} = {bound:.10f}")

    if exact_sum is not None:
        print(f"{'Точное значение':30} = {exact_sum:.10f}")
        print(f"\nПроверка (оценка снизу ≤ точному значению):")
        for name, bound in lower_bounds.items():
            is_valid = bound <= exact_sum
            status = "✓" if is_valid else "✗"
            print(f"{name:30} {status} {bound:.10f} ≤ {exact_sum:.10f}")

    # Визуализация для небольших n
    if n <= 1000:
        x_vals = list(range(1, n + 1))
        harmonic_partial = [sum(1 / i for i in range(1, k + 1)) for k in x_vals]
        lower_bound_vals = [np.log(k) + gamma for k in x_vals]

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, harmonic_partial, 'b-', label=f'H_n (гармонический ряд)')
        plt.plot(x_vals, lower_bound_vals, 'r--', label='ln(n) + γ (оценка снизу)')
        plt.xlabel('n')
        plt.ylabel('Значение')
        plt.title(f'Гармонический ряд H_n и оценка снизу')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    return lower_bounds


# Вычисление для n = 1,000,000
n = 1000000
bounds = harmonic_series_lower_bound(n)

# Дополнительная информация
print(f"\nДополнительная информация:")
print(f"H_{n} ≈ ln({n}) + γ + 1/(2×{n}) - 1/(12×{n}²) + ...")
print(f"ln({n}) = {np.log(n):.10f}")
print(f"γ (постоянная Эйлера) ≈ 0.5772156649")
print(f"Таким образом, H_{n} > {np.log(n) + 0.57721:.10f}")