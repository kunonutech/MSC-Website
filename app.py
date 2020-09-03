from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/Mfuko wa daktari")
def mfuko_daktari():
    return "Hey Future Doctors .The world is yours." \
           "Focus on your future "


if __name__ == '__main__':
    app.run(debug=True)
