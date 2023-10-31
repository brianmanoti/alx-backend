#!/usr/bin/env python3
""" The main entry point for  o-app.py """


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_file():
    """ module to return the index page """
    return render_template('index.html')

