# logic/strategy_legendary.py

def legendary_strategy(history):
    """
    history — список коэффициентов, от последнего к первому (пример: [1.01, 1.45, 2.12, 0.95, 1.3])
    """

    # Определение проигрыша
    def is_loss(k, target): return k < target

    last_k = history[:5]  # Берём последние 5 игр для анализа
    base_bet = 100
    current_bet = base_bet
    step = "start"
    auto_cashout = 1.3

    if not history:
        return {"action": "wait", "reason": "Недостаточно данных"}

    # 1. Последний коэффициент — больше или равен 1.3? Начальная ставка.
    if not is_loss(last_k[0], 1.3):
        return {
            "action": "bet",
            "step": step,
            "bet": base_bet,
            "cashout": auto_cashout,
            "confidence": "95%"
        }

    # 2. Один проигрыш (последний — меньше 1.3)
    if is_loss(last_k[0], 1.3) and not is_loss(last_k[1], 1.3):
        step = "step2"
        return {
            "action": "bet",
            "step": step,
            "bet": base_bet * 2,
            "cashout": 1.5,
            "confidence": "85%"
        }

    # 3. Два проигрыша подряд
    if is_loss(last_k[0], 1.3) and is_loss(last_k[1], 1.3):
        # Ждём фиолетового (например, коэффициент > 5.0)
        for k in last_k[2:]:
            if k >= 5.0:
                step = "step3"
                return {
                    "action": "bet",
                    "step": step,
                    "bet": base_bet * 6,
                    "cashout": 1.5,
                    "confidence": "95%"
                }
        return {
            "action": "wait",
            "step": "wait_purple",
            "reason": "Ждём фиолетового (5x+)"
        }

    return {
        "action": "wait",
        "reason": "Нейтральная зона"
    }
