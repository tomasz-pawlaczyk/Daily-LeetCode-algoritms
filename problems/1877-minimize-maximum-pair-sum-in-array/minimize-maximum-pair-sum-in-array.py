class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums)//2):
            current_sum = nums[i] + nums[len(nums) - 1 - i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
        