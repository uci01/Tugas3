from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template("beranda.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

@app.route("/credit")
def credit():
    return render_template("credit.html")

if __name__ == "__main__":
    app.run(debug=True)
