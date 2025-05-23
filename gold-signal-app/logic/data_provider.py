# logic/data_provider.py

import requests
from bs4 import BeautifulSoup

def get_latest_history(limit=10):
    """
    Получение последних коэффициентов с сайта LuckyJet.
    """
    url = "https://1wvteh.com/casino/play/1play_1play_luckyjet?p=agwi"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример: поиск элементов с классом 'coefficient'
    elements = soup.find_all(class_='coefficient')
    history = []

    for el in elements[:limit]:
        try:
            coef = float(el.text.strip())
            history.append(coef)
        except ValueError:
            continue

    return history
