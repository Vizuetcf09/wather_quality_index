# Librerias

import joblib
import numpy as np

# Modulos

from flask import Flask, app
from flask import jsonify # herramienta para trabajar cno arch json

# servidos

app = Flask(__name__)

#POSTMAN PARA PRUEBAS
@app.route('/', methods=['GET'])

def predict():
    
    """Funcion que se expondra en la direccion 8080/predict y que muestra la prediccion hecha
    por nuestro modelo que exportamos al archivo best_model.pkl
    """
    
    X_test = np.array([5.58,39.92,14.175,5172.0,925.0,52.8])
    prediction = model.predict(X_test.reshape(1, -1))
    
    return jsonify({f'Prediccion: {prediction[0]}'})


if __name__ == "__main__":
    
    model = joblib.load('./models/best_model.pkl')
    app.run(port=6060)