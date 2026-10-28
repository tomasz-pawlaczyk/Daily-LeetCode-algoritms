class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        def invert(v):
            if v == 0:
                return 1
            return 0

        for row in image:
            left, right = 0, len(row)-1
            while left <= right:
                pomoc = row[left]
                row[left] = invert(row[right])
                row[right] = invert(pomoc)
                left += 1
                right -= 1

        return image
        

# Lepszy
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == row[right]:
                    row[left] = row[right] = 1 - row[left]
                left += 1
                right -= 1
        return image