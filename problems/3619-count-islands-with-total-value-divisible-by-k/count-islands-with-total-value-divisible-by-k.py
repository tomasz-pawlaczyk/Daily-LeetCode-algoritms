class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        width = len(grid[0])
        height = len(grid)

        def floodFill(x, y):
            stack = [(x,y)]
            island_sum = 0

            while len(stack) > 0:
                item = stack.pop()
                nx, ny = item[0], item[1]
                if nx < 0 or nx > width - 1:
                    continue
                if ny < 0 or ny > height - 1:
                    continue

                value = grid[ny][nx]
                if value == 0:
                    continue
                island_sum += value
                grid[item[1]][item[0]] = 0

                stack.append((nx-1, ny))
                stack.append((nx+1, ny))
                stack.append((nx, ny-1))
                stack.append((nx, ny+1))

            return island_sum

        result = 0
        for x in range(0, width):
            for y in range(0, height):
                value = floodFill(x, y)
                if value % k == 0 and value > 0:
                    result += 1

        return result

        