# Mahalanobis-distances

Computes (row-wise) Mahalanobis distances given a 2D Numpy array.

# Methodology

* Obtain the principal components of the input matrix M
* Scale each PC
* Computes the Euclidean distances of row pairs (i,j) over the PC space

# Notes

Only the upper half and diagonal outputs are actually computed since the matrix is symetric.

Euclidean distances over the scaled eigenbasis of M is equivalent to Mahalanobis distances over the original space.

Proof:

v_cov = V = t(L) I L   (Cholesky)

x* = Lx     (Principal components with unit variance)
inv_L x* = x

Mal(x, y) = t(inv_L (x* - y*)) inv_(t(L) I L) (inv_L (x* - y*))
= t(x* - y*) (x* - y*)
= Euclidean distance between x* and y*

