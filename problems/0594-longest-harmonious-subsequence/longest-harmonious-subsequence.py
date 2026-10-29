# Czas O(n*logn), pamięć O(1) - poza TimSortem
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            elif nums[right] == nums[left] + 1:
                result = max(result, right-left+1)
                right += 1
            else:
                left += 1
        return result



# Czas O(n), pamięć O(k)
# class Solution:
#     def findLHS(self, nums: list[int]) -> int:
#         from collections import Counter
#         counter = Counter(nums)
#         result = 0
#         for key, value in counter.items():
#             if key+1 in counter:
#                 result = max(result, value + counter[key+1])
#         return result
