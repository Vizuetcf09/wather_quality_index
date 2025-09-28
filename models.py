# Librerias

import pandas as pd
import numpy as np
from sklearn import utils

# Modulos

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

import warnings 
warnings.filterwarnings("ignore")

### Modulo 'utils'

from utils import Utils


# Creamos la clase llamada 'Models'


class Models:

    def __init__(self):
        
        self.reg = {
            'RFR' : RandomForestRegressor(),
        }    

        ### Diccionario de parametros para el modelo de 'RandomForestRegressor()'  

        self.parameters = { # Diccionario de diccionario para los parametros de c/ modelo
                'RFR':{
                    'n_estimators': range(4, 16), # cuantos arboles compondran mi arbol
                    'criterion': ['friedman_mse', 'absolute_error'], 
                    'max_depth': range(2, 11)}, # de dos a 10
        }
      
    # Función de definición del codigo
  

    ### Entrenamiento  

    def grid_training(self, X, y): 

        """Metodo para seleccionar al mejor modelo con el mejor score
        
        Trabaja sobre los atributos, que son diccionarios de modelos y 
        sus respectivos rangos y opciones de parámetros. Se utiliza el optimizador
        Grid y se selecciona finalmente el mejor modelo y el que mas score entrega
        de estos. 
        """
        
        # parametros recibidos

        ### Definimos nuestros 
        best_params = None # se actualiza cuando encontramos un mejor "score"
        best_model = None # se actializa cuando encontramos un mejor "score"
    

        for name, reg in self.reg.items():
          
            rand_est = RandomizedSearchCV(reg, self.parameters[name], n_iter = 5, cv = 3, scoring = 'neg_mean_absolute_error').fit(X, y)
            best_params = rand_est.best_params_        # estimators = np.real(rand_est.best_estimator_)
            best_model = rand_est.best_estimator_
        
        utils = Utils()
        Utils.model_export(self, best_params, best_model) # best_model, best_params
        
        print(best_params)
        print(best_model)