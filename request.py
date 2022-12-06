# -*- coding: utf-8 -*-
"""
@author: Ines Taous and Elise
"""
import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Administrative':10, 
                            'Administrative':10, 
                            'Informational':60,
                            'Informational_Duration':3,
                            'ProductRelated':1000,
                            'ProductRelated_Duration':0,
                            'PageValues':0,
                            'Moyenne_Administrative':2,
                            'Moyenne_Informational':12,
                            'Moyenne_ProductRelated': 1,
                            'weekend_values':12,
                            'month_sin':12,
                            'month_cos':12})

print(r.json())