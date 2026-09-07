class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(0, numRows):
            triangle.append([0]*(i+1))
            for j in range(i+1):
                liczba = -1
                if j == 0 or j == i:
                    liczba = 1
                else:
                    liczba = triangle[i-1][j-1] + triangle[i-1][j]
                
                triangle[i][j] = liczba

        return triangle



        