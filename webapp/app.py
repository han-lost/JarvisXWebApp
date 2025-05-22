from flask import Flask, render_template, request
from strategies import analyze_last_games, gold_drop_chance

app = Flask(__name__)

# Пример последних коэффициентов игры LuckyJet
MOCK_HISTORY = [1.2, 1.3, 2.5, 5.6, 15.0, 0.8, 2.3, 3.0, 12.0, 20.5]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signal')
def signal():
    analysis = analyze_last_games(MOCK_HISTORY)
    return f"Сигнал: {analysis}"

@app.route('/gold')
def gold():
    chance = gold_drop_chance(MOCK_HISTORY)
    return f"Шанс выпадения золотого икса: {chance}%"

if __name__ == '__main__':
    app.run(debug=True)
