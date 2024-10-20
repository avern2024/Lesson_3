def calculate_structure_sum(structure):
    total_sum = 0

    if isinstance(structure, (int, float)):  # Если элемент число, добавляем его к сумме
        total_sum += structure
    elif isinstance(structure, str):  # Если элемент строка, добавляем длину строки
        total_sum += len(structure)
    elif isinstance(structure, (list, tuple, set)):  # Если элемент список, кортеж или множество
        for item in structure:
            total_sum += calculate_structure_sum(item)  # Рекурсивно обходим элементы
    elif isinstance(structure, dict):  # Если элемент словарь
        for key, value in structure.items():
            total_sum += calculate_structure_sum(key)  # Обходим ключи
            total_sum += calculate_structure_sum(value)  # Обходим значения

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)