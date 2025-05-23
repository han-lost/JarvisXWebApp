def expert_strategy(history):
    golds = [x for x in history if x >= 10]

    if len(golds) >= 1:
        return {"signal": "После золота – 2 ставки на 2x, 100–200"}
    else:
        return {"signal": "Ожидаем золото"}