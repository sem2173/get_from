#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def get_movies():
    if request.method =='POST':
        movieapi=request.form['film']
        return render_template('index.html', movieapi=movieapi)    
    return render_template('index.html')
  

if __name__ == "__main__":
    app.run(debug=True)