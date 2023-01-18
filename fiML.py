import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# load the model from a file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    # get the input data from the front-end
    data = request.get_json()

    # make predictions using the model
    predictions = model.predict(data)

    # return the predictions to the front-end
    return jsonify(predictions)
