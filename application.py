import pickle
from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app=application

## import regresor and scaler pickle
ridge_model = pickle.load(open("models/ridge_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method =="POST":
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))

        data = {
            "Temperature": Temperature,
            "RH": RH,
            "Ws": Ws,
            "Rain": Rain,
            "FFMC": FFMC,
            "DMC": DMC,
            "ISI": ISI,
            "Classes": Classes,
            "Region": Region
        }

        df = pd.DataFrame(data, index=[0])
        df = scaler.transform(df)
        prediction = ridge_model.predict(df)

        return render_template('home.html', result=prediction)

    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")