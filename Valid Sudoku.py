# 本质上就是检查当前元素是否在所在行/列/九宫格中出现过，行和列就是i，j，但是九宫格需要推导，这个推导是本题的难点之一

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                box_index = i // 3 * 3 + j // 3

                if (num in rows[i] or num in cols[j] or num in boxes[box_index]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True
