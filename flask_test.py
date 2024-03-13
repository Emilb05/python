from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Emil Berg Halldórsson, sem er bestur í heimi</p>"
app.run()