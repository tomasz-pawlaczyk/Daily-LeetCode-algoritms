class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        result = 0

        def floodFill(x, y):
            if x < 0 or x >= len(grid[0]):
                return
            if y < 0 or y >= len(grid):
                return 
            
            if grid[y][x] == 0:
                grid[y][x] = 1
                floodFill(x+1, y)
                floodFill(x-1, y)
                floodFill(x, y+1)
                floodFill(x, y-1)

        for x in range(len(grid[0])):
            floodFill(x, 0)
            floodFill(x, len(grid) - 1)
        for y in range(len(grid)):
            floodFill(0, y)
            floodFill(len(grid[0]) - 1, y)

        for x in range(1, len(grid[0])-1):
            for y in range(1, len(grid)-1):
                if grid[y][x] == 0:
                    result += 1
                    floodFill(x, y)
        
        return result





# Wersja ze stackiem - stosem
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        result = 0

        def floodFill(x, y):
            stos = [(x, y)]
            while stos:
                cx, cy = stos.pop()
                if cx < 0 or cx >= len(grid[0]):
                    continue
                if cy < 0 or cy >= len(grid):
                    continue
                if grid[cy][cx] == 0:
                    grid[cy][cx] = 1
                    stos.append((cx + 1, cy))
                    stos.append((cx - 1, cy))
                    stos.append((cx, cy + 1))
                    stos.append((cx, cy - 1))

        for x in range(len(grid[0])):
            floodFill(x, 0)
            floodFill(x, len(grid) - 1)
        for y in range(len(grid)):
            floodFill(0, y)
            floodFill(len(grid[0]) - 1, y)

        for x in range(1, len(grid[0]) - 1):
            for y in range(1, len(grid) - 1):
                if grid[y][x] == 0:
                    result += 1
                    floodFill(x, y)

        return result

        