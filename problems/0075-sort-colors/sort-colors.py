class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, iteration, fast = 0, 0, len(nums)-1
        while iteration <= fast:            
            if nums[iteration] == 0:
                nums[slow], nums[iteration] = nums[iteration], nums[slow]
                slow += 1
                iteration += 1
            elif nums[iteration] == 2:
                nums[iteration], nums[fast] = nums[fast], nums[iteration]
                fast -= 1
            else:
                iteration += 1

            
            
# Pierwotny kod - byłem blisko
# class Solution:
#     def sortColors(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         slow, iteration, fast = 0, 1, len(nums)-1
#         while iteration <= fast:            
#             if nums[iteration] == 0:
#                 nums[slow], nums[iteration] = nums[iteration], nums[slow]
#                 slow += 1
#                 iteration = slow + 1
#             elif nums[iteration] == 2:
#                 nums[iteration], nums[fast] = nums[fast], nums[iteration]
#                 fast -= 1
#                 iteration = slow + 1
#             else:
#                 if nums[slow] == 2:
#                     nums[slow], nums[iteration] = nums[iteration], nums[slow]
#                 elif nums[fast] == 0:
#                     nums[fast], nums[iteration] = nums[iteration], nums[fast]
#                 else:
#                     iteration += 1
#         return