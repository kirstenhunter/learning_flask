from flask import Flask
from flask import request
app=Flask(__name__)

from flask import render_template

@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html', food=food)
