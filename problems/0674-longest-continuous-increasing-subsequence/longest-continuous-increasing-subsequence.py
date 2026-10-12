class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        result = 1
        obecny = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                obecny += 1
                if obecny > result:
                    result = obecny
            else:
                obecny = 1
        return result
                
        