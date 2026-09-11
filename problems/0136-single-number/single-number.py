class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        wynik = nums[0]
        for i in range(1, len(nums)):
            wynik ^= nums[i]
        return wynik
        