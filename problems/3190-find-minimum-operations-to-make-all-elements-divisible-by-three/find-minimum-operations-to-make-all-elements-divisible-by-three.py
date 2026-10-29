class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if num % 3 != 0:
                counter += 1
        return counter