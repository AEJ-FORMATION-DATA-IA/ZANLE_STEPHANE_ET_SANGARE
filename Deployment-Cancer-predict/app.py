import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
'''
def data_patient():
    feature = [int(x) for x in request.form.values()]
    data = [pd.read_csv(feature)]
    return data

def var_quantitative():
    var_numer=data_patient()._get_numeric_data().columns
    return var_numer
def normalisation():
    var_numer=var_quantitative()
    df=data_patient()
    for col in var_numer:
            df[col] = df[col] / df[col].max()
    return df

def recoder(serie):
    return serie.astype('category').cat.codes

def encodage():
    df1=normalisation()
    for  i in data_patient().select_dtypes("object").columns:
        df1[i]=recoder(df1[i])
    return df1


'''

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    '''
    For rendering results on HTML GUI
    int
    '''

    data_patient = {
        "AGE": int(request.form['AGE']),
        "SEXE": request.form['SEXE'],
        "TDT": request.form['TDT'],
        "PAR": int(request.form['PAR']),
        "CHOLESTEROL": int(request.form['CHOLESTEROL']),
        "GAJ": int(request.form['GAJ']),
        "ECG": request.form['ECG'],
        "FCMAX": int(request.form['FCMAX']),
        "ANGINE": request.form['ANGINE'],
        "DEPRESSION ": float(request.form['DEPRESSION']),
        "PENTE": request.form['PENTE'],
    }

    '''

    features = [int(x) for x in request.form.values()]
  '''
    final_features = [pd.read_csv(data_patient)]

    #data_final=encodage()


    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('REPONSE.html', prediction_text='Votre etat de santé est:$ {}'.format(output))


if __name__ == "__main__":
    print("hello")
    app.run(debug=True)


