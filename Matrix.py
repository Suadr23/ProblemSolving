#problem(Matrix):
def DiagonalDifference(matrix):
    n = len(matrix)
    sum1_sum = 0
    sum2_sum = 0

    for i in range(n):
        sum1_sum += matrix[i][i]
        sum2_sum += matrix[i][n - 1 - i]

    return abs(sum1_sum - sum2_sum)

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
matrix2 = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(DiagonalDifference(matrix1))
print(DiagonalDifference(matrix2))



