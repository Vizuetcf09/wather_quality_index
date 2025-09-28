# librerias
import pandas as pd
import numpy as np
# modulos
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

import warnings 
warnings.filterwarnings("ignore")

# Algoritmo

### Iniciamos el programa
if __name__ == "__main__":
    
    ## leemos los archivos

    ### leemos el archivo y especificamos la hoja que usaremos como df
    dataset = pd.read_excel('./train/ica_sup_1.xlsx')

    ## tratamiento de los valores atipicos y nulos

    ### eliminar los valores nulos
    data_dropna = dataset.dropna()
    
    ### cambia los valores atipicos por 0
    data_rep = data_dropna.replace({'<30':30, '<3':3, '<2':2, '<10':10})
    ### eliminamos las columnas que no usaremos

    data = data_rep.drop('SITIO', axis = 1)
    print(data.shape, data.dtypes)
    
    #   --- Preparación de los datos
    
    # Separación del df
    
    ## es importante que exista una correlacion  entre las features y la variable que queremos predecir y no es necesarios que los features la tengan    
    
    X = data.drop(['SEMAFORO', 'NUM_SEMAFORO'], axis=1)
    y = data[['NUM_SEMAFORO']]
    
    ### regresor
    reg = RandomForestRegressor()
    
    parameters = {
        'n_estimators': range(4, 16), # cuantos arboles compondran mi arbol
        'criterion': ['friedman_mse', 'absolute_error'], 
        'max_depth': range(2, 11) # de dos a 10
    }
    
    ### son 10 iteracion del optimizador. Toma 10 combinaciones al azar del diccionario, cv = 3, parte en 3 parte el set de datos que le pasemos, para hacer Cross validation
    rand_est = RandomizedSearchCV(reg, parameters, n_iter = 5, cv = 3, scoring = 'neg_mean_absolute_error').fit(X, y)
    
    print(rand_est.best_estimator_)
    print(rand_est.best_params_)
    X_test = np.array([5.58,39.92,14.175,5172.0,925.0,52.8])
    y_hat = rand_est.predict(X_test.reshape(1, -1))
    print(f'Valor real: {y.loc[13]}')
    print({f'Prediccion: {y_hat[0]}'})