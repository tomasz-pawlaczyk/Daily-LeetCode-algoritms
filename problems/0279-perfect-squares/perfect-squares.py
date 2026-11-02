# Bottom - up, od dołu do góry
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)  # minimalna liczba perfect squares konieczna do uzyskania 'i'
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1

        for liczba in range(1, n+1):
            i = 0
            minimalna = float('inf')
            while i < len(squares) and squares[i] <= liczba:
                minimalna = min(minimalna, dp[liczba - squares[i]])
                i += 1
            dp[liczba] = minimalna + 1  # bo nie uwzględnialiśmy dodania aktualnego kwadratu

        return dp[-1]



# Top - down z memoizacją
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        squares = set()
        i = 1
        while i*i <= n:
            squares.add(i*i)
            i += 1

        def calculate(x):
            if x in squares:
                return 1
            
            if x not in memo:
                minimum = float('inf')
                for square in squares:
                    if square <= x:
                        minimum = min(minimum, calculate(x-square))
                memo[x] = minimum + 1
            
            return memo[x]

        return calculate(n)
                


# Top down wykonany przez czata:
# from functools import cache
# import math

# class Solution:
#     def numSquares(self, n: int) -> int:
#         squares = [i * i for i in range(math.isqrt(n), 0, -1)]  # malejąco

#         @cache
#         def calculate(x):  # calculate(m) = minimalna liczba kwadratów dających sumę x
#             if x == 0:
#                 return 0
#             best = float("inf")
#             for sq in squares:
#                 if sq <= x:
#                     best = min(best, calculate(x - sq) + 1)
#             return best

#         return calculate(n)