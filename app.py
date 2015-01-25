#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def get_movies():
    if request.method =='POST':
        film = request.form['film'].strip().replace(" ","+")
        url = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'.format(film)
        omdb_request = requests.get(url)
        omdb_result = omdb_request.json()
        return render_template('index.html', film=film, omdb_request=omdb_result)    
    return render_template('index.html')
  
def urlFormat(film):
    return ''

if __name__ == "__main__":
    app.run(debug=True)



# # -*- coding: utf-8 -*-
# from flask import Flask, url_for, render_template, request
# from format_name import *
# import requests
# app = Flask(__name__)
# @app.route('/', methods=['GET','POST'])
# def api_root():
# if request.method == 'POST':
# movie_name= format_name(request.form['movie_name'])
# url = "http://www.omdbapi.com/?t={0}&y=&plot=short&r=json".format(movie_name)
# omdb_request = requests.get(url)
# omdb_result = omdb_request.json()
# return render_template("index.html", movie_name=movie_name, omdb_request=omdb_result)
# return render_template("index.html")
# if __name__ == '__main__':
# app.run(debug = True)