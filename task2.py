import json

# TODO решите задачу
def task(filepath) -> float:
    # Чтение данных из JSON файла
    with open(filepath) as f:
        data = json.load(f)
    # Вычисление суммы произведений двух значений в каждом словаре с использованием генератора
    sum = round(sum(dictionary.get("score", 0) * dictionary.get("weight", 0) for dictionary in data), 3)


print(task("input.json"))
