class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        result = [[0] * len(board[0]) for _ in range(len(board))]
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    for k in directions:
                        if -1 < i + k[0] < len(board) and -1 < j + k[1] < len(board[0]):
                            result[i + k[0]][j + k[1]] += 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if result[i][j] == 3:
                        board[i][j] = 1
                else:
                    if result[i][j] < 2 or result[i][j] > 3:
                        board[i][j] = 0