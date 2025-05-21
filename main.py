
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
admin_password = "jarvispass"
latest_signal = "Нажми кнопку, чтобы получить сигнал."

@app.route("/", methods=["GET", "POST"])
def index():
    global latest_signal
    if request.method == "POST":
        return render_template("index.html", signal=latest_signal)
    return render_template("index.html", signal=None)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global latest_signal
    if request.method == "POST":
        if request.form.get("password") == admin_password:
            signal = request.form.get("signal")
            if signal:
                latest_signal = signal
            return render_template("admin.html", success=True, signal=latest_signal)
        else:
            return render_template("admin.html", error="Неверный пароль")
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
