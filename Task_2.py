import csv
import timeit
from BTrees.OOBTree import OOBTree
import pandas as pd

# 1. Завантаження даних із CSV
file_path = 'generated_items_data.csv'


def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            item_id = int(row['ID'])
            item = {
                'ID': item_id,  # Include ID in the item dictionary
                'Name': row['Name'],
                'Category': row['Category'],
                'Price': float(row['Price'])
            }
            data.append(item)  # Append the dictionary directly
    return data


data = load_data(file_path)

# 2. Ініціалізація структур
tree = OOBTree()
dict_store = {}

# 3. Функції додавання
def add_item_to_tree(item):
    tree[item['ID']] = item


def add_item_to_dict(item):
    dict_store[item['ID']] = item


# Додавання товарів
for item in data:
    add_item_to_tree(item)
    add_item_to_dict(item)

# 4. Функції діапазонного запиту за Price для OOBTree та dict
def range_query_tree(min_price, max_price):
    # Оскільки OOBTree відсортовано, можна використовувати items(min, max)
    return [item for _, item in tree.items(min_price, max_price) if min_price <= item['Price'] <= max_price]


def range_query_dict(min_price, max_price):
    # Лінійний пошук для словника
    return [item for item in dict_store.values() if min_price <= item['Price'] <= max_price]


# 5. Вимірювання часу для 100 запитів
min_price, max_price = 10, 50
num_queries = 100

time_tree = timeit.timeit(lambda: range_query_tree(min_price, max_price), number=num_queries)
time_dict = timeit.timeit(lambda: range_query_dict(min_price, max_price), number=num_queries)

# 6. Результати
print(f"📦 Total time for 100 range queries:")
print(f"OOBTree: {time_tree:.6f} seconds")
print(f"Dict:    {time_dict:.6f} seconds\n")

print(f"⏱️ Average time per query:")
print(f"OOBTree: {time_tree / num_queries:.6f} seconds")
print(f"Dict:    {time_dict / num_queries:.6f} seconds")

print("_____________________________________")
data = pd.read_csv(file_path)
print(data.head())  # Показує перші 5 рядків