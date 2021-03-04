
import sys
sys.path.append('../src')
from matrix import Matrix

def Matrix_elements_test(M, reference_matrix_elements):
    print('Testing matrix equality...')
    if M.is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_inequality_test(M, reference_matrix_elements):
    print('Testing matrix inequality...')
    if not M.is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_copy_test(M, reference_matrix_elements):
    print('Testing method copy...')
    if M.copy().is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_add_test(M, N, reference_matrix_elements):
    print('Testing method add...')
    if M.add(N).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_subtract_test(M, N, reference_matrix_elements):
    print('Testing method subtract...')
    if M.subtract(N).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_scalar_multiply_test(M, a, reference_matrix_elements):
    print('Testing method scalar multiply...')
    if M.scalar_multiply(a).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_multiply_test(M, N, reference_matrix_elements):
    print('Testing method matrix multiply...')
    if M.matrix_multiply(N).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_size_test(M, rows, cols):
    print('Testing attributes num_rows/num_cols...')
    if M.num_rows == rows and M.num_cols == cols:
        print('PASSED')
        return True
    else:
        return False

def Matrix_transpose_test(M, reference_matrix_elements):
    print('Testing method transpose...')
    if M.transpose().is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

A = Matrix([[1,0,2,0,3],
                [0,4,0,5,0],
                [6,0,7,0,8],
                [-1,-2,-3,-4,-5]])

assert(Matrix_size_test(A, 4, 5))
print()

ref_elts = [[ 1,  0,  6, -1],
 [ 0,  4,  0, -2],
 [ 2,  0,  7, -3],
 [ 0,  5,  0, -4],
 [ 3,  0,  8, -5]]
 
assert(Matrix_transpose_test(A, ref_elts))
print()

A_t = A.transpose()
B = A_t.matrix_multiply(A)
ref_elts = [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
assert(Matrix_multiply_test(A_t, A, ref_elts))
print()


C = B.scalar_multiply(0.1)
ref_elts = [[3.8,  .2, 4.7,  .4, 5.6],
 [ .2, 2.0,  .6, 2.8, 1.0],
 [4.7,  .6, 6.2, 1.2, 7.7],
 [ .4, 2.8, 1.2, 4.1, 2.0],
 [5.6, 1.0, 7.7, 2.0, 9.8]]
assert(Matrix_scalar_multiply_test(B, 0.1, ref_elts))
print()

D = B.subtract(C)
ref_elts = [[34.2,  1.8, 42.3,  3.6, 50.4],
 [ 1.8, 18 ,  5.4, 25.2,  9 ],
 [42.3,  5.4, 55.8, 10.8, 69.3],
 [ 3.6, 25.2, 10.8, 36.9, 18. ],
 [50.4,  9. , 69.3, 18. , 88.2]]
assert(Matrix_subtract_test(B, C, ref_elts))
print()

E = D.add(C)
ref_elts = [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
assert(Matrix_elements_test(B, ref_elts))
print()
assert(Matrix_inequality_test(C, ref_elts))
print()