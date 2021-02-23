
class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def copy(self):
        return  Matrix(self.elements)

    def add(self, M):
        R = Matrix([[0,0], [0,0]])
        R.elements[0][0] = self.elements[0][0] + M.elements[0][0]
        R.elements[0][1] = self.elements[0][1] + M.elements[0][1]
        R.elements[1][0] = self.elements[1][0] + M.elements[1][0]
        R.elements[1][1] = self.elements[1][1] + M.elements[1][1]
        return R
        
    def subtract(self, M):
        R = Matrix([[0,0], [0,0]])
        R.elements[0][0] = self.elements[0][0] - M.elements[0][0]
        R.elements[0][1] = self.elements[0][1] - M.elements[0][1]
        R.elements[1][0] = self.elements[1][0] - M.elements[1][0]
        R.elements[1][1] = self.elements[1][1] - M.elements[1][1]
        return R

    def scalar_multiply(self, a):
        R = Matrix([[0,0], [0,0]])
        R.elements[0][0] = a * self.elements[0][0] 
        R.elements[0][1] = a * self.elements[0][1]
        R.elements[1][0] = a * self.elements[1][0]
        R.elements[1][1] = a * self.elements[1][1]
        return R

    def matrix_multiply(self, M):
        R = Matrix([[0,0], [0,0]])
        R.elements[0][0] = self.elements[0][0] * M.elements[0][0] + \
            self.elements[0][1] * M.elements[1][0]
        R.elements[0][1] = self.elements[0][0] * M.elements[0][1] + \
            self.elements[0][1] * M.elements[1][1]
        R.elements[1][0] = self.elements[1][0] * M.elements[0][0] + \
            self.elements[1][1] * M.elements[1][0]
        R.elements[1][1] = self.elements[1][0] * M.elements[0][1] + \
            self.elements[1][1] * M.elements[1][1]
        return R