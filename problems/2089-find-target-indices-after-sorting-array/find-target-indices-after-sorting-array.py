class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = 0
        equals = 0
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                equals += 1
        
        return list(range(smaller, smaller + equals))  



# class Solution:
#     def targetIndices(self, nums: list[int], target: int) -> list[int]:
#         result = []
#         nums.sort()
#         n = len(nums)
        
#         left, right = 0, n - 1
#         while left <= right:
#             middle = (left + right) // 2
#             if nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = middle - 1
#             else:
#                 result.append(middle)
#                 i = middle + 1
#                 while i < n and nums[i] == target:
#                     result.append(i)
#                     i += 1
#                 i = middle-1
#                 while i >= 0 and nums[i] == target:
#                     result.append(i)
#                     i -= 1
#                 break
#         return sorted(result)