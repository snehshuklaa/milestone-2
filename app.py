from flask import Flask, render_template, request
import pickle
import numpy as mp
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('student-marks-predictor.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
   return render_template('login.html')

standard_to = StandardScaler()
 
  
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
       study_hours = int(request.form.get("study_hours"),False) 
       prediction = model.predict([[study_hours]])[0][0].round(2)
       if study_hours<0 or study_hours>24:
            return render_template('login.html', prediction_text='Please enter valid input')
       else: 
            return render_template('login.html', prediction_text='If you are studying for {} hours a day , you will score around {} percentage marks! keep studying!!').format(int(study_hours),prediction) 
           
       
    else:
        return render_template('login.html')
 
if __name__ == "__main__":
   app.run(debug=True)