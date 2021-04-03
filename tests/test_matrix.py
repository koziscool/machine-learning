
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

def Matrix_pivot_row_test(M, column_index, pivot_row):
    print('Testing method get_pivot_row('+ str(column_index) +')...')
    if M.get_pivot_row(column_index) == pivot_row:
        print('PASSED')
        return True
    else:
        return False

def Matrix_swap_rows_test(M, row_index1, row_index2, reference_matrix_elements):
    print('Testing method swap_rows(' + str(row_index1) + ', ' + str(row_index2) + ')...')
    if M.swap_rows(row_index1, row_index2).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_normalize_row_test(M, row_index, reference_matrix_elements):
    print('Testing method normalize_row('+ str(row_index) +')...')
    if M.normalize_row(row_index).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_clear_below_test(M, row_index, reference_matrix_elements):
    print('Testing method clear_below('+ str(row_index) +')...')
    if M.clear_below(row_index).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_clear_above_test(M, row_index, reference_matrix_elements):
    print('Testing method clear_above('+ str(row_index) +')...')
    if M.clear_above(row_index).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_rref_test(M, reference_matrix_elements):
    print('Testing method rref...')
    if M.rref().is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_augment_test(M, N, reference_matrix_elements):
    print('Testing method augment...')
    if M.augment(N).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_get_rows_test(M, row_nums, reference_matrix_elements):
    print('Testing method get_rows...')
    if M.get_rows(row_nums).is_equal(Matrix(reference_matrix_elements)):
        print('PASSED')
        return True
    else:
        return False

def Matrix_get_columns_test(M, col_nums, reference_matrix_elements):
    print('Testing method get_columns...')
    if M.get_columns(col_nums).is_equal(Matrix(reference_matrix_elements)):
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

print("Testing row reduction on the following matrix")
print( """
[[0, 1, 2],
 [3, 6, 9],
 [2, 6, 8]]
""")

A = Matrix([[0, 1, 2],
 [3, 6, 9],
 [2, 6, 8]])

assert(Matrix_pivot_row_test(A, 0, 1))
print()

assert(Matrix_swap_rows_test(A, 0, 1, [[3, 6, 9], [0, 1, 2], [2, 6, 8]] ))
print()
A = A.swap_rows(0,1)

assert(Matrix_normalize_row_test(A, 0, [[1.0, 2.0, 3.0], [0, 1, 2], [2, 6, 8]] ))
A = A.normalize_row(0)
print()

assert(Matrix_clear_below_test(A, 0, [[1, 2, 3], [0, 1, 2], [0, 2, 2]] ))
A = A.clear_below(0)
print()

assert(Matrix_pivot_row_test(A, 1, 1))
print()

assert(Matrix_normalize_row_test(A, 1, [[1, 2, 3], [0, 1, 2], [0, 2, 2]] ))
A = A.normalize_row(1)
print()

assert(Matrix_clear_below_test(A, 1, [[1, 2, 3], [0, 1, 2], [0, 0, -2]] ))
A = A.clear_below(1)
print()

assert(Matrix_pivot_row_test(A, 2, 2))
print()

assert(Matrix_normalize_row_test(A, 2, [[1, 2, 3], [0, 1, 2], [0, 0, 1]] ))
A = A.normalize_row(2)
print()

assert(Matrix_clear_above_test(A, 2, [[1, 2, 0], [0, 1, 0], [0, 0, 1]] ))
A = A.clear_above(2)
print()

assert(Matrix_clear_above_test(A, 1, [[1, 0, 0], [0, 1, 0], [0, 0, 1]] ))
A = A.clear_above(1)
print()

A = Matrix([[0, 1, 2],
                [3, 6, 9],
                [2, 6, 8]])

A_rref = [[1, 0, 0],
[0, 1, 0],
[0, 0, 1]]
assert(Matrix_rref_test(A, A_rref))
print()

B = Matrix([[0, 0, -4, 0],
                [0, 0, 0.3, 0],
                [0, 2, 1, 0]])

B_rref = [[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 0]]
assert(Matrix_rref_test(B, B_rref))
print()

A = Matrix([
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10, 11, 12]
])
B = Matrix([
    [13, 14],
    [15, 16],
    [17, 18]
])

A_augmented = A.augment(B)
result = [
    [1, 2,   3,  4, 13, 14],
    [5, 6,   7,  8, 15, 16],
    [9, 10, 11, 12, 17, 18]
]
assert(Matrix_augment_test(A, B, result))
print()

result = [
    [1, 2,   3,  4, 13, 14],
    [9, 10, 11, 12, 17, 18]
]
assert(Matrix_get_rows_test(A_augmented, [0,2], result))
print()

result = [
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10, 11, 12]
]
assert(Matrix_get_columns_test(A_augmented, [0,1, 2, 3], result))
print()

result = [
    [13, 14],
    [15, 16],
    [17, 18]
]
assert(Matrix_get_columns_test(A_augmented, [4, 5], result))
print()
