class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        def tribonaci(i):
            if len(dp) > i:
                return dp[i]
            return tribonaci(i-1) + tribonaci(i-2) + tribonaci(i-3)

        for num in range(3, n+1):
            if num >= len(dp):
                dp.append(tribonaci(num))

        return dp[n]