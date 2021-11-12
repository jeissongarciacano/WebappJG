from flask import Blueprint
from flask.templating import render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/Fibonacci')
def Fibonacci():
    return render_template("Fibonacci.html")

@views.route('/Factorial')
def Factorial():
    return render_template("Factorial.html")

@views.route('/APtriangulo')
def APtriangulo():
    return render_template("APtriangulo.html")

@views.route('/APrectangulo')
def APrectangulo():
    return render_template("APrectangulo.html")

@views.route('/APcirculo')
def APAPcirculo():
    return render_template("APcirculo.html")


