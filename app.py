
from flask import Flask,render_template,request
import joblib
import numpy as np

app= Flask(__name__,template_folder='web')

@app.route('/')
def car():
    return render_template("home.html")

def AvgPredictor(speed):
    to_predict = np.array([[speed]])
    loaded_model = joblib.load('model.sav')
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/',methods=['POST','GET'])

def result():

    if request.method == 'POST':
        speed = request.form['Avg']
        result = (AvgPredictor(int(speed)))
        return render_template("home.html", result=result)

    else:
        return "Value out of range"

if __name__ == '__main__':
    app.run(debug=True)