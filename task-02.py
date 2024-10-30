import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2 + 1

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою, межі 0-2
ix = np.linspace(0, 2)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=0, color='gray', linestyle='--')
ax.axvline(x=2, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2+1 від 0 до 2')


# перевірка чи точка вище лінії, чи нижче
def is_inside(x, y):
    return y <= (x ** 2 + 1)  # x ** 2 + 1

def monte_carlo_simulation(num_experiments):
    average_area = 0

    x_borders = [0, 2]
    y_borders = [0, 6]
    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(*x_borders), random.uniform(*y_borders)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (2 * 6)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area

# Кількість експериментів
num_experiments = 1000

# Виконання симуляції
average_area = monte_carlo_simulation(num_experiments)
print(f"Інтеграл визначений через monte-carlo, за {num_experiments} експериментів: {average_area}")


# Перевірка результатів отриманих по монте-карло
def f(x):
    return x**2 + 1

# Обчислення інтеграла, межі 0-2
result, error = spi.quad(f, 0, 2)

print("Інтеграл визначений через scipy: ", result, error)

plt.grid() 
plt.show() # можна побудувати графік