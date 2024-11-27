import numpy as np

def calculate(list):

    if len(list) !=9:
        raise valueError("List must contain nine numbers.")
  
    list=np.array(list).reshape((3,3))

    Calculations={}
    Calculations['mean']=[list.mean(axis=0).tolist(),list.mean(axis=1).tolist(), np.mean(list).tolist()]
    Calculations['variance']=[list.var(axis=0).tolist(),list.var(axis=1).tolist(), np.var(list).tolist()]
    Calculations['standard deviation']=[list.std(axis=0).tolist(),list.std(axis=1).tolist(), np.std(list).tolist()]
    Calculations['max']=[list.max(axis=0).tolist(),list.max(axis=1).tolist(), np.max(list).tolist()]
    Calculations['min']=[list.min(axis=0).tolist(),list.min(axis=1).tolist(), np.min(list).tolist()]
    Calculations['sum']=[list.sum(axis=0).tolist(),list.sum(axis=1).tolist(), np.sum(list).tolist()]
    return Calculations
