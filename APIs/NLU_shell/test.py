import requests
import numpy as np

base="http://127.0.0.1:5000/"
payload={"input_str":"What is the accuracy?"}
r = requests.get(base, params=payload).json()
print(r['result'])
