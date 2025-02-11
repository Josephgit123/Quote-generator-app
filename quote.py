from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    response = requests.get("https://api.quotable.io/random").json()
    return response

if __name__ == "__main__":
    app.run(debug=True)
