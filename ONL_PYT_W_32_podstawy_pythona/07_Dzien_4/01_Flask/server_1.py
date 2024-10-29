from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Witaj użytkowniku!"


@app.route("/hello/<imie>")
def hello_somebody(imie):
    return f"Witaj {imie}, miło cię poznać!"


if __name__ == "__main__":
    app.run(debug=True)
