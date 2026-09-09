# 分享两个做法，一个是碰到边界或者已经访问过的元素就转向，显然转向的规则是确定的（逆时针）所以可以通过维护一个方向向量来看下一元素的当方位，时间复杂度是O(m*n)
# 维护矩阵的边界，每次遇到边界就将边界的范围缩小，选哟注意到的是要考虑只有一行或只有一列的情况，这两种情况可以通过加入判断避免出错

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        seq = []
        direction = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while len(seq) < n*m:
            seq.append(matrix[i][j])
            matrix[i][j] = "visited"
            d_i, d_j = directions[direction]
            next_i = i + d_i
            next_j = j + d_j

            if next_j >= n or next_i >= m or next_j < 0 or next_i < 0 or matrix[next_i][next_j] == "visited":
                direction = (direction + 1) % 4
                d_i, d_j = directions[direction]
                next_i = i + d_i
                next_j = j + d_j
            
            i = next_i
            j = next_j
        return seq
m = Solution()
print(m.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        seq = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        left = 0
        right = n - 1
        bottom = m - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                seq.append(matrix[top][j])
            
            top += 1

            for i in range(top, bottom + 1):
                seq.append(matrix[i][right])
            
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    seq.append(matrix[bottom][j])
            
            bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    seq.append(matrix[i][left])
            
            left += 1

        return  seq
m = Solution()
print(m.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
