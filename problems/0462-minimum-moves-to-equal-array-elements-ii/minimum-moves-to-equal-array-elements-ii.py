class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        counter = 0
        for num in nums:
            counter += abs(num - median)

        return counter
        