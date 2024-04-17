from flask import Flask# test

app = Flask(__name__)# more test

@app.route("/")
def hello_world():# more tests
    # issue?
    return "<center><p>Emil Berg Halldórsson, sem er bestur í heimi</p><center>"
print("let's start running")# fun
app.run()# yea, more tests

#yey