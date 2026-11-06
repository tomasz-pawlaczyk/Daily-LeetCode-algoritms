class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        # dp[y][x] - najmniejszy koszt stanięcia w polu (x, y) 
        dp = [[float('inf')] * (width + 1) for _ in range(height + 1)]
        dp[0][1] = 0

        for y in range(1, height + 1):
            for x in range(1, width + 1):
                field = grid[y-1][x-1]
                dp[y][x] = min(dp[y-1][x] + field, dp[y][x-1] + field)

        # print(*dp, sep="\n")
        return dp[-1][-1]


# Wersja z pamięcią O(1)
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        for y in range(0, height):
            for x in range(0, width):
                if x == 0 and y == 0:
                    continue
                elif x == 0:
                    grid[y][x] += grid[y-1][x]
                elif y == 0:
                    grid[y][x] += grid[y][x-1]
                else:
                    grid[y][x] += min(grid[y-1][x], grid[y][x-1])

        # print(*grid, sep="\n")
        return grid[-1][-1]