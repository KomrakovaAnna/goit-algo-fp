import numpy as np
import matplotlib.pyplot as plt

#  кількість кидків
num_rolls = 1000000

#  кидки для двох кубиків
rolls_1 = np.random.randint(1, 7, num_rolls)
rolls_2 = np.random.randint(1, 7, num_rolls)

# Обчислюємо суми чисел, які випали на кубиках
sums = rolls_1 + rolls_2

# скільки разів випала кожна можлива сума
sum_counts = np.bincount(sums)[2:]  # індекси 0 і 1 не використовуються

#  ймовірність кожної суми
probabilities = sum_counts / num_rolls

#  графік для візуалізації ймовірностей
plt.bar(range(2, 13), probabilities, color='blue', alpha=0.7)
plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--')
plt.show()

for i, prob in enumerate(probabilities, start=2):
    print(f"Сума {i}: {prob:.4f} або {prob*100:.2f}%")
