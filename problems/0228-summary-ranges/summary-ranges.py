class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lista = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i+1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                lista.append(f"{start}")
            else:
                lista.append(f"{start}->{nums[i]}")
            i += 1

        return lista



# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         a = None
#         b = None
#         lista = []

#         for i in range(0, len(nums)):
#             if a == None:
#                 a = nums[i]
#                 if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
#                     lista.append(f"{a}")
#                     a = None
#                     b = None

#             else:
#                 if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
#                     b = nums[i]
#                     lista.append(f"{a}->{b}")
#                     a = None
#                     b = None
#         return lista
        

