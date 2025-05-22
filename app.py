from flask import Flask, render_template, request
from strategies import give_signal, gold_rate
from config import ADMIN_PASSWORD

app = Flask(__name__)

@app.route('/')
def panel():
    return render_template('panel.html')

@app.route('/signal', methods=['POST'])
def signal():
    if request.form.get("password") == ADMIN_PASSWORD:
        result = give_signal()
    else:
        result = "Доступ запрещен"
    return render_template('panel.html', output=result)

@app.route('/gold', methods=['POST'])
def gold():
    if request.form.get("password") == ADMIN_PASSWORD:
        result = gold_rate()
    else:
        result = "Доступ запрещен"
    return render_template('panel.html', output=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
