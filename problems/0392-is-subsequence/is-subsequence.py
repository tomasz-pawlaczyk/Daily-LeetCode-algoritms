# Two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_left, t_left = 0, 0

        while s_left < len(s) and t_left < len(t):
            if s[s_left] == t[t_left]:
                s_left += 1
                t_left += 1
            else:
                t_left += 1

        if s_left == len(s):
            return True
        return False



# Programowanie dynamiczne dla ćwiczenia
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # czy pierwsze `i` znaków stringa `s` można znaleźć jako subsekwencję w pierwszych `j` znakach stringa `t`.
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        dp[0] = [1] * (len(t) + 1)

        for y in range(1, len(s) + 1):
            for x in range(1, len(t) + 1):
                if s[y-1] == t[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                else:
                    dp[y][x] = dp[y][x-1] # dodawanie znaków 't' nie zmienia faktu, że znaleziono subsekwencję

        return bool(dp[-1][-1])

#     s
#     ||
#   t=[1, a, h, b, g, d, c]
#     [a, 1, 1, 1, 1, 1, 1]
#     [b, 0, 0, 1, 1, 1, 1]
#     [c, 0, 0, 0, 0, 0, 1]