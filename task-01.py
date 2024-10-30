import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість Лимонад
B = pulp.LpVariable('B', lowBound=0, cat='Integer')  # Кількість Фруктовий Сік

# Функція цілі (Максимізація прибутку)
model += A + B, "Profit"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для води
model += 1 * A <= 50           # Обмеження для цукру
model += 1 * A <= 30           # Обмеження для лимонного соку
model += 2 * B <= 40           # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонад:", A.varValue)
print("Виробляти фруктовий сік:", B.varValue)
