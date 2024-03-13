from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Emil Berg, ég er glaðasti glaðasti meistari í heimi, mér er fagnað á hverjum degi og ég fíla það</p>"
app.run()