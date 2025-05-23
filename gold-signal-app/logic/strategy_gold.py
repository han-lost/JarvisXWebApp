# logic/strategy_gold.py

def generate_signal(history):
    """
    Пример реализации стратегии на основе истории коэффициентов.
    """
    if not history:
        return {"signal": "Недостаточно данных"}

    average = sum(history) / len(history)
    if average > 2.0:
        return {"signal": "Ставить на 2x"}
    else:
        return {"signal": "Ожидать"}
