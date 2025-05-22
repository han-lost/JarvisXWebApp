import random

def give_signal():
    x = random.uniform(1.5, 10)
    return f"Сигнал: ожидаемый икс = {round(x, 2)}"

def gold_rate():
    chance = random.randint(5, 20)
    return f"Шанс золотого икса в следующей игре: {chance}%"
