class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        posiadam = -float('inf')
        nieposiadam = 0

        for price in prices:
            nowe_posiadam = max(posiadam, nieposiadam - price)
            nowe_nieposiadam = max(nieposiadam, posiadam + price)

            posiadam = nowe_posiadam
            nieposiadam = nowe_nieposiadam

        return nieposiadam



