# module_4_1.py
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызовов функций
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Вывод результатов в консоль
print(result1)  # 23.0
print(result2)  # Ошибка
print(result3)  # 7.0
print(result4)  # inf