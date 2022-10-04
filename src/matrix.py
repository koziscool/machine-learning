
def dot_product(u,v):
    ret_val = 0
    if len(u) == len(v):
        for i in range(len(u)):
            ret_val += u[i] * v[i]
        return ret_val


class Matrix:
    def __init__(self, elements):
        self.elements = elements.copy()
        self.num_rows = len(elements)
        self.num_cols = len(elements[0])

    def row(self, r):
        return self.elements[r]

    def col(self, c):
        ret_arr = []
        for i in range(self.num_rows):
            ret_arr.append(self.elements[i][c])
        return ret_arr
        
    def new_zero_matrix(self, num_rows, num_cols):
        M = []
        for i in range(num_rows):
            arr = []
            for j in range(num_cols):
                arr.append(0)
            M.append(arr)
        return Matrix(M)

    def copy(self):
        copied_elements = [[entry for entry in row] for row in self.elements]
        return Matrix(copied_elements)

    def add(self, M):
        if self.num_rows == M.num_rows and self.num_cols == M.num_cols:
            R = self.new_zero_matrix(self.num_rows, self.num_cols)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    R.elements[i][j] = self.elements[i][j] + M.elements[i][j]
            return R
        
    def subtract(self, M):
        if self.num_rows == M.num_rows and self.num_cols == M.num_cols:
            R = self.new_zero_matrix(self.num_rows, self.num_cols)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                   R.elements[i][j] = self.elements[i][j] - M.elements[i][j]
            return R

    def scalar_multiply(self, a):
        R = self.new_zero_matrix(self.num_rows, self.num_cols)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                   R.elements[i][j] = a * self.elements[i][j]
        return R

    def matrix_multiply(self, M):
        if self.num_cols == M.num_rows:
            R = self.new_zero_matrix(self.num_rows, M.num_cols)
            for i in range(self.num_rows):
                for j in range(M.num_cols):
                   R.elements[i][j] = dot_product(self.row(i), M.col(j)) 
            return R

    def transpose(self):
        R = self.new_zero_matrix(self.num_cols, self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                   R.elements[j][i] = self.elements[i][j]
        return R

    def is_equal(self, M):
        if self.num_rows != M.num_rows or self.num_cols != M.num_cols:
            return False
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                   if round(self.elements[i][j], 3) != round(M.elements[i][j], 3):
                       return False
        return True

    def get_pivot_row(self, column_index):
        for i in range(self.num_rows):
            bool_left_zeros = True
            for j in range(column_index):
                if self.elements[i][j] != 0:
                    bool_left_zeros = False
            if bool_left_zeros and self.elements[i][column_index] != 0:
                return i
        return None

    def swap_rows(self, row_index1,row_index2):
        ret_M = self.copy()
        temp = ret_M.elements[row_index1]
        ret_M.elements[row_index1] = ret_M.elements[row_index2]
        ret_M.elements[row_index2] = temp
        return ret_M

    def normalize_row(self, row_index):
        ret_M = self.copy()
        row = ret_M.elements[row_index]
        scale_factor, elt_index = 0, 0
        while scale_factor == 0 and elt_index < len(row):
            scale_factor = row[elt_index]
            elt_index += 1
        if scale_factor != 0:
            for elt_index in range(len(row)):
                row[elt_index] /= scale_factor
        ret_M.elements[row_index] = row
        return ret_M

    def clear_below(self, row_index):
        ret_M = self.copy()
        row = ret_M.row(row_index)
        key_index, i  = -1, 0

        while key_index == -1 and i < len(row):
            if row[i] != 0:
                key_index = i
                break
            i += 1
     
        if key_index != -1:
            for i in range(row_index + 1, len(ret_M.elements)):
                multiplier = ret_M.elements[i][key_index] / row[key_index]
                for j in range(len(ret_M.elements[i])):
                    ret_M.elements[i][j] -= multiplier * row[j]

        return ret_M

    def clear_above(self, row_index):
        ret_M = self.copy()
        row = ret_M.row(row_index)
        key_index, i  = -1, 0

        while key_index == -1 and i < len(row):
            if row[i] != 0:
                key_index = i
                break
            i += 1
        
        if key_index != -1:
            for i in range(row_index):
                multiplier = ret_M.elements[i][key_index] / row[key_index]
                for j in range(len(ret_M.elements[i])):
                    ret_M.elements[i][j] -= multiplier * row[j]
        
        return ret_M

    def rref(self):
        ret_M = self.copy()
        row_index = 0
        for column_index in range(ret_M.num_cols):
            pivot_index = ret_M.get_pivot_row(column_index)
            if not pivot_index == None:
                if not pivot_index == row_index:
                    ret_M = ret_M.swap_rows(row_index, pivot_index)
                ret_M = ret_M.normalize_row(row_index)
                ret_M = ret_M.clear_above(row_index)
                ret_M = ret_M.clear_below(row_index)
                row_index += 1
        return ret_M

    def augment(self, B):
        if self.num_rows != B.num_rows:
            return None

        ret_M = []
        for i in range(self.num_rows):
            temp_arr = []
            for j in range(self.num_cols):
                temp_arr.append(self.elements[i][j])
            for j in range(B.num_cols):
                temp_arr.append(B.elements[i][j])
            ret_M.append(temp_arr)
        return Matrix(ret_M)

    def get_rows(self, row_nums):
        ret_M = []
        for i in range(self.num_rows):
            if i in row_nums:
                temp_arr = []
                for j in range(self.num_cols):
                    temp_arr.append(self.elements[i][j])
                ret_M.append(temp_arr)
        return Matrix(ret_M)

    def get_columns(self, col_nums):
        ret_M = []
        for i in range(self.num_rows):
                temp_arr = []
                for j in range(self.num_cols):
                    if j in col_nums:
                        temp_arr.append(self.elements[i][j])
                ret_M.append(temp_arr)
        return Matrix(ret_M)

    def inverse(self):
        if self.num_rows != self.num_cols:
            print("Error: cannot invert a non-square matrix")
            return "non-square"

        I = identity_matrix(self.num_rows)
        M = self.copy().augment(I)
        RREF = M.rref()
        identity_range, inverse_range = [*range(self.num_cols)], [*range(self.num_cols, 2*self.num_cols)]            
        I_test = RREF.get_columns(identity_range)
        if I.is_equal(I_test):
            return RREF.get_columns(inverse_range)
        else:
            print('Error: cannot invert a singular matrix')
            return "non-singular"

    def determinant(self):
        def normalize(M, row_index):
            M_copy = M.copy()
            row = M_copy.elements[row_index]
            scale_factor, elt_index = 0, 0
            while scale_factor == 0 and elt_index < len(row):
                scale_factor = row[elt_index]
                elt_index += 1
            if scale_factor != 0:
                for elt_index in range(len(row)):
                    row[elt_index] /= scale_factor
            M_copy.elements[row_index] = row
            return M_copy, scale_factor

        if self.num_rows != self.num_cols:
            print('Error: cannot take determinant of a non-square matrix')
            return "non-square"

        M = self.copy()
        row_index, scale_product, num_swaps = 0, 1, 0
        for column_index in range(M.num_cols):
            scale_factor = 0
            pivot_index = M.get_pivot_row(column_index)
            if not (pivot_index == None):
                if not pivot_index == row_index:
                    M = M.swap_rows(row_index, pivot_index)
                    num_swaps += 1
                M, scale_factor = normalize(M, row_index)
                M = M.clear_above(row_index)
                M = M.clear_below(row_index)
                row_index += 1
                scale_product *= scale_factor

        if M.is_equal(identity_matrix(M.num_cols)):
            return ((-1) ** num_swaps) * scale_product
        else:
            return 0

    def cofactor_method_determinant(self):
        def get_minor(M, strike_row, strike_col):
            ret_M = []
            for i in range(M.num_rows):
                if i != strike_row:
                    temp_arr = []
                    for j in range(M.num_cols):
                        if j != strike_col:
                            temp_arr.append(M.elements[i][j])
                    ret_M.append(temp_arr)
            return Matrix(ret_M)

        if self.num_rows != self.num_cols:
            print('Error: cannot take determinant of a non-square matrix')
            return "non-square"
        
        if self.num_rows == 1:
            return self.elements[0][0]

        ret_val, row = 0, 0
        for col in range(self.num_cols):
            ret_val += ((-1) ** (row+col)) * self.elements[row][col] * get_minor(self, row, col).cofactor_method_determinant()
        return ret_val
    
    def __add__(self, M):
       return self.add(M) 

    def __sub__(self, M):
        return self.subtract(M)
        
    def __mul__(self, a):
       return self.scalar_multiply(a)

    def __rmul__(self, a):
       return self.scalar_multiply(a)

    def __matmul__(self, M):
       return self.matrix_multiply(M)

    def __eq__(self, M):
       return self.is_equal(M)

    def exponent(self, exp):
        ret_M = self.copy()
        for _ in range(1, exp):
            ret_M = ret_M.matrix_multiply(self)
        return ret_M

    def __pow__(self, exp):
        return self.exponent(exp)

def identity_matrix(n):
    I_elts =  [[ 1 if j == i else 0 for j in range(n)] for i in range(n) ]
    return Matrix(I_elts)

