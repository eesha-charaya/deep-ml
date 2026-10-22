import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	

    # Numpy 
    if len(a[0]) == len(b):
        return np.matmul(a,b).tolist()
    else:
        return -1

