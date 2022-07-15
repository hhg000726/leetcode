class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        answer = 0
        
        def area(i, j):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + area(i + 1, j) + area(i - 1, j) + area(i, j - 1) + area(i, j + 1)
            else:
                return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    answer = max(answer, area(i, j))
        
        return answer