from flask import Flask

app = Flask(__name__)

@app.route("/")
def goodbye_world():
    return "<h1>Goodbuy, World! Enjoy the Sails and Bar Guns!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
