from flask import Flask, request, jsonify
from sklearn.externals import joblib

app = Flask(__name__)

# load pre-trained model
model = joblib.load("loan_default_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # get loan applicant information from the request
    data = request.get_json(force=True)
    prediction = model.predict_proba([data['credit_score'], data['income'], data['loan_amount'], data['loan_term']])[0]

    # format the response
    output = {'default_probability': prediction[1]}
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
