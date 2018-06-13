#!/usr/bin/env python

# import tensorflow as tf
# # import bottle
# # from bottle import route, run
# import threading
# import json
# import numpy as np

# # from prepro import convert_to_features, word_tokenize
# from time import sleep

from flask import Flask, url_for, render_template, make_response, request, jsonify, redirect
from gevent.wsgi import WSGIServer
'''
This file is taken and modified from R-Net by Minsangkim142
https://github.com/minsangkim142/R-net
'''

# app = bottle.Bottle()
app = Flask(__name__)
print("Flask server running...")
# query = []
# response = ""

@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/answer', methods = ['POST'])
def answer():
    print("inside answer")
    # print(request.form['passage'])
    passage = request.form['passage'] #bottle.request.json['passage']
    question = request.form['question'] #bottle.request.json['question']
    print("received question: {}".format(question))
    # if not passage or not question:
    #     exit()
    print("here")
    # global query, response
    # query = (passage, question)
    # while not response:
    #     sleep(0.1)
    # print("received response: {}".format(response))
    # response_ = {"answer": response}
    # response = []
    response = "brojo"
    return jsonify(answer=response)

# class Demo(object):
#     def __init__(self, model, config):
#         run_event = threading.Event()
#         run_event.set()
#         threading.Thread(target=self.demo_backend, args = [model, config, run_event]).start()
#         # # app.run(port=8080, host='0.0.0.0')
#         http_server = WSGIServer(('', 5000), app)
#         http_server.serve_forever()
#         try:
#             while 1:
#                 sleep(.1)
#         except KeyboardInterrupt:
#             print("Closing server...")
#             run_event.clear()

#     def demo_backend(self, model, config, run_event):
#         global query, response

#         with open(config.word_dictionary, "r") as fh:
#             word_dictionary = json.load(fh)
#         with open(config.char_dictionary, "r") as fh:
#             char_dictionary = json.load(fh)

#         sess_config = tf.ConfigProto(allow_soft_placement=True)
#         sess_config.gpu_options.allow_growth = True

#         with model.graph.as_default():

#             with tf.Session(config=sess_config) as sess:
#                 sess.run(tf.global_variables_initializer())
#                 saver = tf.train.Saver()
#                 saver.restore(sess, tf.train.latest_checkpoint(config.save_dir))
#                 if config.decay < 1.0:
#                     sess.run(model.assign_vars)
#                 while run_event.is_set():
#                     sleep(0.1)
#                     if query:
#                         context = word_tokenize(query[0].replace("''", '" ').replace("``", '" '))
#                         c,ch,q,qh = convert_to_features(config, query, word_dictionary, char_dictionary)
#                         fd = {'context:0': [c],
#                               'question:0': [q],
#                               'context_char:0': [ch],
#                               'question_char:0': [qh]}
#                         yp1,yp2 = sess.run([model.yp1, model.yp2], feed_dict = fd)
#                         yp2[0] += 1


#                         print("received actual response : {}".format(" ".join(context[yp1[0]:yp2[0]])))
#                         # start = max(0,yp1[0]-10)
#                         start = yp1[0]
#                         end = yp2[0]
#                         # response = " ".join(context[yp1[0]:yp2[0]])
#                         response = " ".join(context[start:end])  
                        
#                         print(len(yp1))
#                         print(len(yp2))

#                         print("indexes = " + str(yp1[0]) +" , " + str(yp2[0]))
#                         query = []

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug = True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()