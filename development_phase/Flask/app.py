from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("Diabetes-Prediction.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        
        HighBP = request.form['HighBP']
        HighChol = request.form['HighChol']
        CholCheck = request.form['CholCheck']
        BMI = request.form['BMI']
        Smoker = request.form['Smoker']
        Stroke = request.form['Stroke']
        HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
        PhysActivity = request.form['PhysActivity']
        Fruits = request.form['Fruits']
        Veggies = request.form['Veggies']
        AnyHealthcare = request.form['AnyHealthcare']
        NoDocbcCost = request.form['NoDocbcCost']
        GenHlth = request.form['GenHlth']
        MentHlth = request.form['MentHlth']
        PhysHlth = request.form['PhysHlth']
        DiffWalk = request.form['DiffWalk']
        Sex = request.form['Sex']
        Age = request.form['Age']
        Education = request.form['Education']
        Income = request.form['Income']
        hvyAlcoholConsump = request.form['hvyAlcoholConsump']

        attributes = [
            HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack,
            PhysActivity, Fruits, Veggies, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth,
            PhysHlth, DiffWalk, Sex, Age, Education, Income, hvyAlcoholConsump
        ]

        attributes = [float(attr) if attr.isnumeric() else attr for attr in attributes]
        pred = model.predict([attributes])
        index = ['No Diaabetes', 'Pre Diabetes', 'Diabetes']
        result = "The Diabetes Prediction for this person is: " + index[pred[0]]
        return result  

if __name__=='__main__':
    app.run(debug=True) 