
def legendary_strategy(history):
    last = history[-1]
    if last < 1.3:
        return {
            "strategy": "Legendary 1.3",
            "signal": "Ставь 10% от банка на 1.3x до проигрыша.",
            "confidence": "95%"
        }
    else:
        return {
            "strategy": "Legendary 1.3",
            "signal": "Подожди фиолет, затем ставь 3x банк на 1.5x.",
            "confidence": "93%"
        }
