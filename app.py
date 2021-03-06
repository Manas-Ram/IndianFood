# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_nut_value
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index', methods= ['GET', 'POST'])
def index():
    return render_template("index.html", time=datetime.now())

@app.route('/foods', methods= ['GET', 'POST'])
def foods():
    return render_template("foods.html", time=datetime.now())
@app.route('/result', methods= ['GET', 'POST'])
def result():
    print(request.form)
    ind_food = (request.form["food"])
    quant_v=(request.form["quantity"])
    nut_v=get_nut_value(ind_food, quant_v)
    return render_template("result.html", ind_food=ind_food, quant_v=quant_v, nut_v=nut_v, time=datetime.now())


