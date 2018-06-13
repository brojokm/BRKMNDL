#!/usr/bin/python
from flask import Flask, url_for, render_template, make_response, request, jsonify, redirect
# from urllib import urlencode
# from urlparse import urlparse, parse_qs
# import urllib
# from requests import get
import os
import localize
from gevent.wsgi import WSGIServer
import re
from time import time as tim

app = Flask(__name__)
# app = Flask(__name__, static_folder = '../Flask_files')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
    try:
        start_time = tim()
        q = request.form['query']
        q = q.lower()
        q = q.replace("logn", "log n")
        q = re.sub('\W+',' ', q)

        print("searched query is ")
        print(q)  
        llst=[]

        ll = localize.localizer(q)

        for l in ll:
          lst=[]
          file = "/static/" + str(l[0]) + ".webm"
          lst.append(file)
          lst.append(l[1])
          lst.append(l[2]) ####added on 15th april
          llst.append(lst)
          # print(file)
          # print(l[1])       
        
        # lst = []
        # lst.append("/static/Lec-01-Brief_Overview_of_the_course.webm")
        # lst.append(205) 
        # llst.append(lst)
        # lst = []
        # lst.append("/static/Lec-11-Deuteron-.webm")
        # lst.append(25) 
        # llst.append(lst)
        # lst = []
        # lst.append("/static/Lec-16_Theories_of_nuclear_forces.webm")
        # lst.append(589) 
        # llst.append(lst)
        end_time = tim()
        total_time = end_time - start_time
        print("Time to Response = {} seconds".format(total_time))
        
        return jsonify(query=q, result=llst)
        # path = os.path.abspath(q)
        # return render_template('index.html', llist=llst, query=q)
    except IOError as e:
        print(e)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug = True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()