# Create API of ML model using flask

# Import libraries
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import sklearn
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)

# Load the model
lin_model = pickle.load(open('./ML_Script/ghg_linear_model.pkl','rb'))
poly_model = pickle.load(open('./ML_Script/ghg_poly_model.pkl','rb'))
poly = PolynomialFeatures(degree=3)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
       
        print(request.form['exp'])
        data = float(request.form['exp'])
        print("Data", lin_model.predict([[data]]))
        
        # Make prediction using model loaded from disk as per the data.
        lin_prediction = lin_model.predict([[data]])
        poly_prediction = poly_model.predict(poly.fit_transform([[data]]))
        # Take the first value of prediction
        lin_output = lin_prediction[0]
        poly_output = poly_prediction[0]


        return render_template("results.html", lin_output=lin_output, poly_output = poly_output,exp=data)

@app.route('/visualizations/<html_name>')
def fetch_visual(html_name):
    return render_template("tableau/{}.html".format(html_name))

if __name__ == '__main__':
    app.run(debug=True)
