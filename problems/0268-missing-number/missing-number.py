class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        suma = 0
        while i < len(nums):
            suma -= nums[i]
            suma += i
            i += 1
        suma += i
        return suma



# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         wynik = len(nums)
#         for i, num in enumerate(nums):
#             wynik ^= i ^ num
#         return wynik
        