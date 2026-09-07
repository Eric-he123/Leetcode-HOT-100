# 分享两个做法，第一个方法用的拓扑网络，利用队列进行处理；第二个方法利用DFS的递归，注意利用DFS的递归的时候会TLE，需要一些小trick

# Thought 1
from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        indegree = [[0] * n for _ in range(m)]
# ------------进行入度矩阵的构建------------------
        for i in range(m):
            for j in range(n):
                for r, c in directions:
                    ni = i + r
                    nj = j + c
                    
                    if 0 <= ni < m and 0 <= nj < n and matrix[i][j] > matrix[ni][nj]:
                        indegree[i][j] += 1
# ------------完成入度矩阵的构建------------------
      
        queue = deque()
        length = 0
      
# ------------进行起始点的入队------------------     
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i,j))
# ------------完成起始点的入队------------------    
      
# ------------进行队列内潜在点的处理------------------
        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                i, j = queue.popleft()
                for r, c in directions:
                    ni = i + r
                    nj = j + c
                    if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni,nj))
# ------------完成队列内潜在点的处理------------------
      return length

# Thought 2
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
# -----------用来避免重复运算------------------
        dp = [[-1] * n for _ in range(m)]
      
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            up = dfs(i-1, j, matrix[i][j])
            down = dfs(i+1, j, matrix[i][j])
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])

            dp[i][j] = max(up, down, left, right) + 1
            return dp[i][j]
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j,-1))

        return ans


