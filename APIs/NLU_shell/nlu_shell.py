from flask import Flask, request, jsonify
from flask_restful import Api,Resource,reqparse
from sentence_transformers import SentenceTransformer
import scipy
import numpy as np

app= Flask(__name__)
api=Api(app)
model = SentenceTransformer('bert-base-nli-mean-tokens')

feature_db = { "time":['clock', 'time', 'how many hours', 'minutes',],
		"date":['date', 'calendar',],
		"schedule":['timetable','plan','agenda','task list', 'things to do', 'todo list','work'],
		"music": ['music','play music', 'rythm','melody'],}

feature_db_encoded = {}
for key,v in feature_db.items():
    feature_db_encoded[key]=model.encode(v)


class shell(Resource):
    def post(self):
        query = request.get_json()['sentence']
        query_embedding = model.encode([query])
        results=[]
        for key,value in feature_db_encoded.items():
            distances = scipy.spatial.distance.cdist(query_embedding, value, "cosine")[0]
            results.append(np.mean(distances))
        results = zip(list(feature_db.keys()), results)
        results = sorted(results, key=lambda x: x[1])
        return jsonify({"Most related feature": results[0][0]})


api.add_resource(shell,"/predict")

if __name__ == "__main__":
    app.run(debug=True)
