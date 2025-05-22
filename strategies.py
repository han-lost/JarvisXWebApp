# Простые шаблоны стратегий для анализа
def analyze_last_games(games):
    # Простая заглушка: анализ последних коэффициентов
    if not games:
        return "Недостаточно данных"
    average = sum(games[-10:]) / min(len(games), 10)
    if average < 2:
        return "Ожидается рост"
    elif average > 5:
        return "Скоро падение"
    return "Стабильно"

def gold_drop_chance(games):
    golds = [x for x in games if x >= 10]
    return round(len(golds) / len(games) * 100, 2) if games else 0
