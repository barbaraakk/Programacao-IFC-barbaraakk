from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola():
    return "<h1>Oi</h1>"

app.run(debug=True, host="0.0.0.0", port=5010)