class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        slownik = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in slownik:
                if i - slownik[num] <= k:
                    return True
            slownik[num] = i
        return False




# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(0, len(nums)-1):
#             for j in range(i+1, min(i+k+1, len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
        