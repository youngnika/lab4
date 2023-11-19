import json

# TODO решите задачу
def task(filepath) -> float:
    # Чтение данных из JSON файла
    with open(filepath) as f:
        data = json.load(f)
    # Вычисление суммы произведений двух значений в каждом словаре с использованием генератора
    summa = round(sum(dictionary.get("score", 0) * dictionary.get("weight", 0) for dictionary in data), 3)
    return summa


print(task("input.json"))
