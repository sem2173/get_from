#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def get_movies():
    if request.method =='POST':
        film = request.form['film']
        url = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'.format(film)
        omdb_request = requests.get(url)
        omdb_result = omdb_request.json()
        return render_template('index.html', film=film, omdb_request=omdb_result)    
    return render_template('index.html')
  

if __name__ == "__main__":
    app.run(debug=True)



