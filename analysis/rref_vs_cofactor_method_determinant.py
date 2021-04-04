
import sys
sys.path.append('../src')
from matrix import Matrix
import random

def counting_across_rows_matrix_elements(m,n):
    return [[ random.randint(1, 4) + i * n + j for j in range(n)] for i in range(m)]

M = Matrix(counting_across_rows_matrix_elements(10, 10))

print(M.elements)
print(M.determinant())
print(M.cofactor_method_determinant())

# the rref method is faster

# the cofactor method is factorial (ie, exponential) time over the length of the underlying matrix
# this is because the number of minors of the matrix, recurively applied, is factorial

# the rref method is quadratic over the length of the underlying matrix
# it has one for-loop each for the rows and columns
