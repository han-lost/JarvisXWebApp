# logic/strategy_legendary.py

def legendary_strategy(history):
    """
    Реализация легендарной стратегии.
    """
    if not history:
        return {"signal": "Недостаточно данных"}

    last = history[-1]
    if last < 1.3:
        return {"signal": "Ставить 10% от банка на 1.3x"}
    elif last < 1.5:
        return {"signal": "Удвоить ставку на 1.5x"}
    else:
        return {"signal": "Ожидать фиолетового иска"}
