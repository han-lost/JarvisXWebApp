def micro_strategy(history):
    if len(history) < 5:
        return {"signal": "Недостаточно данных"}

    if all(x < 1.09 for x in history[-4:]):
        return {"signal": "Ставь 3 раза подряд на 1.1x"}
    else:
        return {"signal": "Ждать"}