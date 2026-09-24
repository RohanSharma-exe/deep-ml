def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for i in matrix:
			means.append(float(sum(i)/len(i)))
	elif mode == "column":
		matrix = [list(row) for row in zip(*matrix)]
		for i in matrix:
			means.append(float(sum(i)/len(i)))
	return means