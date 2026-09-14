class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        widziane = set()
        for num in nums:
            if num in widziane:
                return True
            widziane.add(num)
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))