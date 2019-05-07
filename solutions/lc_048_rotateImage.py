class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # iterate through top left submatrix
        half_size = int(len(matrix)/2)
        for i in range(half_size):  # top half
            for j in range(len(matrix)-half_size):  # left half, middle inclusive if odd
                k1 = len(matrix) - i - 1
                k2 = len(matrix) - j - 1
                matrix[i][j], matrix[j][k1], matrix[k1][k2], matrix[k2][i] = \
                    [matrix[k2][i], matrix[i][j], matrix[j][k1], matrix[k1][k2]]
