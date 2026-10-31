class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Ogólnie używalibyśmy dp[i] jako min koszt stanięcia w 'i' włącznie
        # Skoro stanięcie w 'i' zależy tylko od i-1 lub i-2 to wystarczą dwie zmienne
        i = 2
        prev1 = cost[1]
        prev2 = cost[0]

        while i < len(cost):
            current_step = min(prev1, prev2) + cost[i]
            prev2 = prev1
            prev1 = current_step
            i += 1

        return min(prev1, prev2)