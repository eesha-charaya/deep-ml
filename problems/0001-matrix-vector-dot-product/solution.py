import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	# No numpy
	ans = []
	if not a or not b or len(a[0]) != len(b):
		return -1
	for row in a:
		sum = 0
		for i in range(len(b)):
			sum += row[i] * b[i]
		ans.append(sum)
	return ans

	# List comprehension
	if not a or not b or len(a[0]) != len(b):
		return -1
	return [sum(x*y for x,y in zip(row, b))for row in a]
	
	# Numpy 1
	try:
		return np.matmul(a,b).tolist()
	except ValueError as e:
		return -1 

	# Numpy 2 
	if not a or not b or len(a[0]) != len(b):
		return -1
	a = np.array(a)
	b = np.array(b)
	return a @ b


	