from flask import Flask, render_template, request
from config import ADMIN_TOKEN

app = Flask(__name__)

@app.route('/')
def index():
    is_admin = request.args.get('admin_token') == ADMIN_TOKEN
    return render_template('index.html', is_admin=is_admin)

@app.route('/get_signal')
def get_signal():
    # Вставим позже логику выбора сигнала
    return "Сигнал: X10 скоро!"

@app.route('/gold_chance')
def gold_chance():
    # Вставим позже расчёт шанса золота
    return "Шанс золота: 94%"

if __name__ == '__main__':
    app.run(debug=True)
