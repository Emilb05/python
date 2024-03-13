from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<center><p>Emil Berg Halldórsson, sem er bestur í heimi</p><center>"
print("let's start running")
# issue
app.run()