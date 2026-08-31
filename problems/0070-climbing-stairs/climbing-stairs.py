# TOP-bottom + memoizacja = słownik
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {0:0, 1:1, 2:2}

#         def krok(n):
#             if n in memo:
#                 return memo[n]
#             else:
#                 memo[n] = krok(n-1) + krok(n-2) 
#                 return memo[n]
#         return krok(n)


# BOTTOM-top = 2 zmienne
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        poprzedni, wynik = 1, 2
        for i in range(3, n + 1):
            poprzedni, wynik = wynik, poprzedni + wynik  # ciekawy trik
        return wynik

