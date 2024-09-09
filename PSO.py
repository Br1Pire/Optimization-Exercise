import numpy as np
from pyswarm import pso
import pandas as pd
import time

# Definir la función Mishra 2
def mishra_2(x):
    D = len(x)  # Dimensiones del problema
    summation = np.sum([0.5 * (x[i] + x[i+1]) for i in range(D - 1)])
    exponent = D - summation
    base = 1 + D - summation
    return base ** exponent

def PSO():
    dimension = [10, 30, 50]
    swarmsize = [100, 200, 300, 400, 500]
    maxiter = [200, 300 ,500, 700, 1000]
    global_minimun = 2
    results = []
    for valueD in dimension:

        # Definir los límites de las variables: 0 <= xi <= 1
        lower_bounds = [0] * valueD  
        upper_bounds = [1] * valueD

        for valueS in swarmsize:
            for valiueM in maxiter:
                
                # Ejecutar el algoritmo PSO
                star_time = time.time()
                best_position, best_value = pso(mishra_2, lower_bounds, upper_bounds, swarmsize=valueS, maxiter=valiueM, minfunc=1e-50, minstep=1e-50)
                end_time = time.time()


                results.append([valueD,valueS,valiueM,np.around(best_position, decimals=1),np.around(best_value, decimals=1),end_time-star_time,abs(np.around(best_value, decimals=1)-global_minimun)])

    return results








