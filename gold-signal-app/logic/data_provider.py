import requests
from bs4 import BeautifulSoup

def get_latest_history(limit=10):
    url = "https://1wvteh.com/casino/play/1play_1play_luckyjet?p=agwi"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример парсинга (нужно адаптировать)
    elements = soup.find_all(class_='coefficient')
    history = []

    for el in elements[:limit]:
        try:
            coef = float(el.text.strip().replace("x", ""))
            history.append(coef)
        except:
            continue

    return history