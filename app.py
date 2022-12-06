# -*- coding: utf-8 -*-
"""
@author: Ines Taous and Elise
"""
import numpy as np
import os
import pickle
import sklearn
from flask import Flask,render_template,request,jsonify






app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]

    return render_template('index.html', prediction_text='It is {}'.format(output))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')