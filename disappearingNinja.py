from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Michaelangel')
def Mich():
    return render_template("Michaelangel.html")

@app.route('/Leonardo')
def Leo():
    return render_template("Leonardo.html")

@app.route('/Raphael')
def Raph():
    return render_template("Raphael.html")

@app.route('/donatello')
def dona():
    return render_template("donatello.html")

app.run(debug=True)