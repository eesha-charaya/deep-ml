import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	

    # Numpy 
    if not a or not b or len(a[0]) != len(b):
        return -1
    try:
        return np.matmul(a,b).tolist()
    except ValueError:
        return -1