arr = np.array([[2, 4], [1, 3], [0, 0], [0, 0]])
U, S, VT = np.linalg.svd(arr)
Sigma = np.diag(S)
Sigma_inverse = np.linalg.ОБРАТНАЯ_МАТРИЦА(Sigma)
Sigma_plus = np.concatenate((Sigma_inverse, np.array([[0, 0], [0, 0]]).T), axis=1)
A_plus = Правые_вектора_транспонированные @ Sigma_plus @ Левые_вектора_транспонированные
