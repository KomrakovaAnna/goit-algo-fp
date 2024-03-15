import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth):


    if depth == 0:
        return
    
    # Розрахунок кінцевої точки поточної гілки
    x_end = x + np.cos(np.radians(angle)) * length
    y_end = y + np.sin(np.radians(angle)) * length

    # Малювання гілки
    plt.plot([x, x_end], [y, y_end], 'k-', lw=1)

    new_length = length * 0.8  

    # Рекурсивне малювання правої та лівої гілок
    draw_tree(x_end, y_end, angle - 45, new_length, depth - 1)
    draw_tree(x_end, y_end, angle + 45, new_length, depth - 1)

# Функція для виклику малювання дерева
def pythagoras_tree(depth):
    plt.figure(figsize=(10, 8))
    draw_tree(0, 0, 90, 100, depth)  
    plt.axis('off')  
    plt.show()

pythagoras_tree(8)
