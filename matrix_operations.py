import numpy as np

class MatrixX:
    def __init__(self, matrix):
        """
        Initializes the MatrixX object with a matrix.
        
        :param matrix: 2D list or numpy array (Matrix)
        """
        if not isinstance(matrix, (np.ndarray, list)):
            raise ValueError("Input should be a numpy array or a 2D list.")
        self.matrix = np.array(matrix)

    def multiply(self, other_matrix):
        """
        Multiplies the current matrix with another matrix.
        
        :param other_matrix: Matrix to multiply with
        :return: Resultant matrix after multiplication
        """
        try:
            # Ensure matrices can be multiplied
            return np.dot(self.matrix, other_matrix)
        except ValueError:
            return "Matrix dimensions do not match for multiplication."

    def transpose(self):
        """
        Returns the transpose of the matrix.
        
        :return: Transposed matrix
        """
        return np.transpose(self.matrix)

    def determinant(self):
        """
        Returns the determinant of the matrix.
        
        :return: Determinant of the matrix or error message if not square
        """
        if self.matrix.shape[0] == self.matrix.shape[1]:
            return np.linalg.det(self.matrix)
        else:
            return "Matrix must be square to calculate determinant."

    def inverse(self):
        """
        Returns the inverse of the matrix.
        
        :return: Inverse of the matrix or error message if not invertible
        """
        if self.matrix.shape[0] == self.matrix.shape[1]:
            try:
                return np.linalg.inv(self.matrix)
            except np.linalg.LinAlgError:
                return "Matrix is singular and cannot be inverted."
        else:
            return "Matrix must be square to calculate inverse."

# Example usage:
if __name__ == "__main__":
    matrix_1 = MatrixX([[1, 2], [3, 4]])
    matrix_2 = MatrixX([[5, 6], [7, 8]])

    print("Matrix 1:")
    print(matrix_1.matrix)

    print("\nMatrix 2:")
    print(matrix_2.matrix)

    # Matrix multiplication
    print("\nMatrix Multiplication:")
    print(matrix_1.multiply(matrix_2.matrix))

    # Transpose
    print("\nTranspose of Matrix 1:")
    print(matrix_1.transpose())

    # Determinant
    print("\nDeterminant of Matrix 1:")
    print(matrix_1.determinant())

    # Inverse
    print("\nInverse of Matrix 1:")
    print(matrix_1.inverse())
