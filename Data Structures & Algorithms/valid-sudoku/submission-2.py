class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = (
            collections.defaultdict(set),
            collections.defaultdict(set),
            collections.defaultdict(set),
        )

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i]:
                    return False
                elif board[i][j] in col[j]:
                    return False
                elif board[i][j] in square[(i // 3, j // 3)]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])

        return True
