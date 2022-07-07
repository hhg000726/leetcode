class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        x, y = 0, 0
        answer = [matrix[0][0]]
        while len(answer) < len(matrix) * len(matrix[0]):
            if -1 < x + directions[d][1] < len(matrix[0]) and -1 < y + directions[d][0] < len(matrix) and matrix[y + directions[d][0]][x + directions[d][1]] < 101:
                matrix[y][x] = 101
                x += directions[d][1]
                y += directions[d][0]
                answer.append(matrix[y][x])
            else:
                d += 1
                if d == 4:
                    d = 0
        return answer