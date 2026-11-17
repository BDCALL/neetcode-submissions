class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range (9):
            for j in range (9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                c_row = (i, num)
                c_col = (num, j)
                combined = (i // 3, j//3, num)
                if c_row in seen or c_col in seen or combined in seen:
                    return False
                seen.add(c_row)
                seen.add(c_col)
                seen.add(combined)
        return True
