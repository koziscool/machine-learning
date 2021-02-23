
import sys
sys.path.append('../src')
from matrix import Matrix

def Matrix_equality(M, N):
    rows, cols = 2, 2
    for i in range(rows):
        for j in range(cols):
            if M[i][j] != N[i][j]:
                return False
    return True

def Matrix_elements_test(M, reference_matrix_elements):
    return Matrix_equality(M.elements, reference_matrix_elements)

def Matrix_copy_test(M, reference_matrix_elements):
    print('Testing method copy...')
    if Matrix_equality(M.copy().elements, reference_matrix_elements):
        print('PASSED')
        return True
    else:
        return False

def Matrix_add_test(M, N, reference_matrix_elements):
    print('Testing method add...')
    if Matrix_equality(M.add(N).elements, reference_matrix_elements):
        print('PASSED')
        return True
    else:
        return False

def Matrix_subtract_test(M, N, reference_matrix_elements):
    print('Testing method subtract...')
    if Matrix_equality(M.subtract(N).elements, reference_matrix_elements):
        print('PASSED')
        return True
    else:
        return False

def Matrix_scalar_multiply_test(M, a, reference_matrix_elements):
    print('Testing method scalar multiply...')
    if Matrix_equality(M.scalar_multiply(a).elements, reference_matrix_elements):
        print('PASSED')
        return True
    else:
        return False

def Matrix_multiply_test(M, N, reference_matrix_elements):
    print('Testing method matrix multiply...')
    if Matrix_equality(M.matrix_multiply(N).elements, reference_matrix_elements):
        print('PASSED')
        return True
    else:
        return False

A = Matrix([[1,3],
                [2,4]])
assert(Matrix_elements_test(A, [[1, 3], [2, 4]]))

B = A.copy()
A = 'resetting A to a string'
assert(Matrix_copy_test(B, [[1, 3], [2, 4]]))
print()

C = Matrix([[1,0],
                [2,-1]])
assert(Matrix_add_test(B, C, [[2, 3], [4, 3]]))
print()

assert(Matrix_subtract_test(B, C, [[0, 3], [0, 5]]))
print()

assert(Matrix_scalar_multiply_test(B, 2, [[2, 6], [4, 8]]))
print()

assert(Matrix_multiply_test(B, C, [[7, -3], [10, -4]]))
print()
