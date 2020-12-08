#!/usr/bin/env python
# coding: utf-8


#import re
#import numpy as np
#from tensorflow.keras.preprocessing.sequence import pad_sequences
#import pickle
#from keras.models import load_model

from flask import Flask, request, render_template
#import gc

#def preprocessing(x):
#    x = x.lower()
#    x = re.sub('\[(.*?)\]', '', x)
#    x = re.sub('[\n]{2,}', '\n',x)
#    x = re.sub("[^a-z\'\s\n]",'',x)
#    x = re.sub('[\n]', ' *newline* ',x)
#    x = re.sub('^\s','',x)
#    x = re.sub('[\s]{2,}', ' ',x)
#    out =np.array( x.split(' ') )
#    out = out[out!= '']
#    return out



#index_to_word =  pickle.load( open( "index_to_word.p", "rb" ) )
#word_to_index =  pickle.load( open( "word_to_index.p", "rb" ) )


#model_load = load_model('mAIchael_buble')

#def make_lyrics( input, n_words):
#    input_p = preprocessing(input)
#    for i in range(n_words):
#        input_pad = pad_sequences( [[word_to_index[word] if word in word_to_index.keys() else 0  for word in input_p ]] , maxlen = 30, padding='pre')
#        predict = model_load.predict_classes(input_pad, verbose=0)[0]
#        if index_to_word[predict] == '*newline*':
#            input = input + '\n'
#        else:
#            input = input +' '+ index_to_word[predict]
#        input_p = np.append(input_p, index_to_word[predict])
#    return input


app = Flask(__name__)

@app.route('/')
def my_form():

    method = request.method
    return render_template('index.html', method= method)

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text =  'Lorem Ipsum'  #make_lyrics( text, 50)

    song = processed_text.replace('\n', '<br>')
    method = request.method

    return render_template('index.html', method= method, song = song)


app.run(threaded=True, port=5000)
