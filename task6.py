def greedy_algorithm(items, budget):
    # Сортування страв за співвідношенням калорійності до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, attrs in sorted_items:
        if total_cost + attrs["cost"] <= budget:
            selected_items.append(item)
            total_cost += attrs["cost"]
            total_calories += attrs["calories"]
    
    return selected_items, total_cost, total_calories

### Алгоритм динамічного програмування


def dynamic_programming(items, budget):
    item_list = list(items.keys())
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = items[item_list[i-1]]["cost"]
            calories = items[item_list[i-1]]["calories"]
            if cost <= w:
                dp[i][w] = max(calories + dp[i-1][w-cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    # Відновлення набору вибраних страв та обчислення загальної вартості
    selected_items = []
    w = budget
    total_cost = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_list[i-1])
            w -= items[item_list[i-1]]["cost"]
            total_cost += items[item_list[i-1]]["cost"]
    
    selected_items.reverse()  # правильний порядок додавання страв
    total_calories = dp[n][budget]
    
    return selected_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Жадібний алгоритм:", greedy_result)
print("Динамічне програмування:", dp_result)
