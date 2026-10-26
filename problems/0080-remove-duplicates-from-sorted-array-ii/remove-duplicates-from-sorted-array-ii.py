# Licznik 
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         counter = 1
#         slow = 0
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 counter += 1
#             else:
#                 if counter > 1:
#                     nums[slow+1] = nums[slow]
#                 slow += min(counter, 2)
#                 nums[slow] = nums[i]
#                 counter = 1
#         if counter > 1:
#             slow += 1
#             nums[slow] = nums[slow-1]
            
#         return slow + 1


# Dwa wskaźniki
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2    # następne wolne pole w wyniku
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

        