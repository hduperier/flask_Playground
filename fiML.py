import pickle
from flask import Flask, request, jsonify, render_template

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

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/loanPred')
def loanPred():
   return render_template('loanPred.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
