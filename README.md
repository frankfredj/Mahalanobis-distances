# Mahalanobis-distances

Computes (row-wise) Mahalanobis distances given a 2D Numpy array.

# Methodology

* Obtain the principal components of the input matrix M
* Scale each PC
* Computes the Euclidean distances of row pairs (i,j) over the PC space

# Notes

Only the upper half and diagonal outputs are actually computed since the matrix is symetric.

Euclidean distances over the scaled eigenbasis of M is equivalent to Mahalanobis distances over the original space. For a quick proof,
consider the Cholesky decomposition of the variance-covariance matrix, namely the transpose of L multiplied by L itself. By noting that
the unit-variance principal components are spawned by multiplying a given vector y by L, it can be shown that going from PC_y = Ly to y = inv_L PC_y, and substituting for y in the Mahalanobis distance formula, yields the Euclidean distance between y* and an arbitrary vector x*.


