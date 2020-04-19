import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS, cross_origin
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def results():
    data = request.get_json(force=True)

    print(data)

    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]

    return str(output)


if __name__ == "__main__":
    app.run(debug=True)
