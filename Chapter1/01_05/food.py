from flask import Flask
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)

from flask import render_template

@app.route('/dinner/')
@app.route('/dinner/<food>')
def eat(food=None):
    return render_template('food.html', food=food, list=["pizza","pasta","stirfry"])
