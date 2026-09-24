import math
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]
        for i in range(1, n+1):
            if i%2 != 0:
                ans.append(ans[i-1] + 1)
            else:
                binarna = i >> 1
                ans.append(ans[binarna])
        return ans


# Wersja krótsza
# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         ans = [0] * (n + 1)
#         for i in range(1, n + 1):
#             ans[i] = ans[i >> 1] + (i & 1)
#         return ans