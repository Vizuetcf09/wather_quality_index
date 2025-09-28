from utils import Utils
from models import Models

if __name__ == "__main__":
    
    ### indica la ejecución de los archivos ".py"
    utils = Utils()
    models = Models()
    
    dataset = utils.load_from_csv('./in/ind_ica.csv')
    X, y = utils.features_target(dataset, ['SEMAFORO', 'NUM_SEMAFORO'], ['NUM_SEMAFORO'])
    
    models.grid_training(X, y)
    
    print(dataset)