import numpy as np
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Матриця пропускної здатності
capacity_matrix = [
        #  0   1   2   3   4   5   6   7   8   9  10 11 12 13 14 15 16 17 18 19 20 21
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0 Супер-джерело (не використовується)
        [0, 0, 0, 25, 20, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1 Термінал 1
        [0, 0, 0, 0, 10, 15, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2 Термінал 2
        [0, 0, 0, 0, 0, 0, 0, 15, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3 Склад 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 10, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4 Склад 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 15, 10, 0, 0, 0, 0, 0, 0],  # 5 Склад 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 15, 5, 10, 0],  # 6 Склад 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 7 Магазин 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 8 Магазин 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 9 Магазин 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 10 Магазин 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 11 Магазин 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 12 Магазин 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 13 Магазин 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 14 Магазин 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 15 Магазин 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 16 Магазин 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 17 Магазин 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 18 Магазин 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 19 Магазин 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9999],  # 20 Магазин 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 21 Супер-сток
    ]

def bfs(capacity_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(capacity_matrix[u]):
            if not visited[v] and capacity > 0:  # Пройти тільки по позитивним пропускним здатностям
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity_matrix, source, sink):
    parent = [-1] * len(capacity_matrix)
    max_flow = 0

    while bfs(capacity_matrix, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity_matrix[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            capacity_matrix[u][v] -= path_flow
            capacity_matrix[v][u] += path_flow
            v = parent[v]

    return max_flow

# Запуск алгоритму для кожного термінала (виходячи з індексації)
source_terminal_1 = 1  # Термінал 1
source_terminal_2 = 2  # Термінал 2
sink_start = 7         # Початкові магазини (індексація з 7 до 20)
sink_end = 20

# Для кожного термінала і магазину вивести потік
def calculate_flow():
    for terminal in range(1, 3):  # Термінали 1 і 2
        for store in range(7, 21):  # Магазини 1 до 14
            temp_capacity_matrix = [row[:] for row in capacity_matrix]
            flow = edmonds_karp(temp_capacity_matrix, terminal, store)
            print(f"Термінал {terminal} -> Магазин {store - 6}: {flow} одиниць")


def show_capacity_from_terminals_to_warehouses():
    for terminal in range(1, 3):  # Термінали 1 і 2
        for warehouse in range(3, 7):  # Склади 1 до 4
            capacity = capacity_matrix[terminal][warehouse]
            if capacity > 0:  # Виводити тільки ті, де є пропускна здатність
                print(f"Термінал {terminal} -> Склад {warehouse - 2}: {capacity} одиниць")

 #візуалізація____________________________________________________________________________________________
def visualize_capacity_full_graph():
    # Створюємо порожній граф
    G = nx.DiGraph()  # Напрямлений граф для зберігання пропускної здатності

    # Додаємо термінали, склади та магазини як вузли
    terminals = [1, 2]  # Термінали
    warehouses = [3, 4, 5, 6]  # Склади
    stores = range(7, 21)  # Магазини

    # Додаємо ребра між терміналами і складами
    for terminal in terminals:
        for warehouse in warehouses:
            capacity = capacity_matrix[terminal][warehouse]
            if capacity > 0:
                G.add_edge(f"Термінал {terminal}", f"Склад {warehouse - 2}", weight=capacity)

    # Додаємо ребра між складами і магазинами
    for warehouse in warehouses:
        for store in stores:
            capacity = capacity_matrix[warehouse][store]
            if capacity > 0:
                G.add_edge(f"Склад {warehouse - 2}", f"Магазин {store - 6}", weight=capacity)

    # Розташування вершин графа з більшими відстанями між терміналами, складами та магазинами
    pos = nx.spring_layout(G, seed=42, k=0.2)  # Коефіцієнт k змінює відстань між вузлами

    # Встановлюємо конкретні координати для терміналів, складів та магазинів
    pos["Термінал 1"] = [0, 3]  # Встановлюємо координати для Терміналів
    pos["Термінал 2"] = [0, -3]

    # Встановлюємо координати для Складів
    pos["Склад 1"] = [-2, 1]
    pos["Склад 2"] = [-2, 0]
    pos["Склад 3"] = [-2, -1]
    pos["Склад 4"] = [-2, -2]

    # Встановлюємо координати для Магазинів
    for i in range(7, 21):
        pos[f"Магазин {i - 6}"] = [2, (i - 6) * 0.3 - 2]  # Всі магазини праворуч

    # Отримуємо ваги (пропускні здатності) для відображення
    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, font_weight="bold", arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Пропускна здатність між Терміналами, Складом та Магазинами", fontsize=14)
    plt.show()


if __name__ == "__main__":
    show_capacity_from_terminals_to_warehouses()

print("___________________________________")

if __name__ == "__main__":
    calculate_flow()

if __name__ == "__main__":
    visualize_capacity_full_graph()
