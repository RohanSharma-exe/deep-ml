def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = []
	b = matrix[0][0] + matrix[1][1]
	c = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	eigenvalues.append(float((b + (((b)**2)-4*c)**(0.5))/(2)))
	eigenvalues.append(float((b - (((b)**2)-4*c)**(0.5))/(2)))
	
	return eigenvalues