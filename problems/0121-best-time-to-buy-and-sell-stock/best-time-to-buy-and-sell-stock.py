class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        utarg_max = 0
        min_cena = float('inf')
        for i in range(0, len(prices)):
            if prices[i] < min_cena:
                min_cena = prices[i]
            else:
                utarg = prices[i] - min_cena
                if utarg > utarg_max:
                    utarg_max = utarg 


        return utarg_max
        