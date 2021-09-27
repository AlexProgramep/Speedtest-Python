from flask import Flask, render_template , url_for , request , redirect
from waitress import serve
from datetime import datetime
from internet_flask import download, upload, ping

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ваш токен'

@app.route("/")
@app.route("/speedtest")
def speedtest():
    now = datetime.now()
    datenow = f"{now.day}.{now.month}.{now.year}  {now.hour}:{now.minute}:{now.second}"
    return render_template("main.html", download=download, upload=upload, ping=ping, datetime=datenow)

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)
    print("http://127.0.0.1:8080")
    app.run(debug=True)