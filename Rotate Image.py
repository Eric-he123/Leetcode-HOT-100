# 顺时针旋转九十度就是先转置再对每一行进行反转，逆时针旋转九十度就是以副对角线进行转置再进行每一列的反转
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:

        for i in range(len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row[:] = row[::-1]
