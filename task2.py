import json

# TODO решите задачу
def task(filepath) -> float:
    # Чтение данных из JSON файла
    with open(filepath) as f:
        data = json.load(f)
    # Вычисление суммы произведений двух значений в каждом словаре
    sum = 0
    for dictionary in data:
        score = dictionary.get("score", 0)
        weight = dictionary.get("weight", 0)
        product = score * weight
        sum += product
    return round(sum,3)


print(task("input.json"))
