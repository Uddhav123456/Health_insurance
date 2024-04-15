from flask import Flask,request,jsonify,render_template
import config
from Project.utils import MedicalInsurance
import numpy as np
# from flask import jsonify

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/predict",methods= ["POST","GET"])
def get_insurance():
    data = request.form
    age = int(data["age"])
    gender = data["gender"]
    bmi = int(data["bmi"])
    children = int(data["children"])
    smoker  = data["smoker"]
    region = data["region"]
    med_obj = MedicalInsurance(age,gender,bmi,children,smoker,region)
    charges = med_obj.get_predict_charges()
    print(charges)

    return render_template('index.html',health_insurance_price=charges)
    
    
if __name__ == "__main__":
    app.run(debug = True)