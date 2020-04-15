import requests
import numpy

url = 'http://localhost:5000/results'
r = requests.post(
    url, json={'male': 1,
               'age': 48,
               'education': 1,
               'currentSmoker': 1,
               'cigsPerDay': 20,
               'BPMeds': 0,
               'prevalentStroke': 0,
               'prevalentHyp': 0,
               'diabetes': 0,
               'totChol': 245,
               'sysBP': 127,
               'diaBP': 80,
               'BMI': 25,
               'heartRate': 75,
               'glucose': 70
               })

# r = requests.post(
#     url, json={'rate': 5, 'sales_in_first_month': 200, 'sales_in_second_month': 400})

print(r.json())
