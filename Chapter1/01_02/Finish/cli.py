import click
from flask import Flask

app = Flask(__name__)

@app.cli.command()
def sayhi():
    """Say Hello."""
    click.echo('Hello')
