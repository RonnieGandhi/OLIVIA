import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/predict" + , json = {"sentence":"what is my plan of work for tomorrow?"})
print(response.json())
