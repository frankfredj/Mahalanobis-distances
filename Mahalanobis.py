def Mahalanobis_Distances(matrix):

	import numpy as np 
	from sklearn.decomposition import PCA

	if str(type(matrix)) != "<class 'numpy.ndarray'>":

		print("Task failed : input needs to be a 2D Numpy Array.")

		return

	def scaler(matrix):

		for i in range(0, np.shape(matrix)[1]):

			matrix[:,i] = (matrix[:,i] - np.mean(matrix[:,i])) / np.std(matrix[:,i])

		return(matrix)


	pca = PCA(n_components=1, svd_solver='full')

	matrix = scaler(pca.fit_transform(matrix))

	n = np.shape(matrix)[0]



	adj_matrix = np.empty(shape = (n,n))

	for j in range(0,n):

		for i in range(0,j+1):

			adj_matrix[i,j] = np.linalg.norm(matrix[i,:] - matrix[j,:])
			adj_matrix[j,i] = adj_matrix[i,j]


	return(adj_matrix)










