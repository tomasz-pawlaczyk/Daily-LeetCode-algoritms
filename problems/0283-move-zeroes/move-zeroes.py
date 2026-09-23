class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        prawo = 1
        for lewo in range(0, len(nums)):
            if nums[lewo] == 0:
                if prawo <= lewo:
                    prawo = lewo + 1
                while prawo < len(nums) and nums[prawo] == 0:
                    prawo += 1
                if prawo < len(nums):
                    nums[lewo], nums[prawo] = nums[prawo], nums[lewo]
                    prawo += 1




# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         zera, liczby = 0, 0
#         while zera < len(nums) and liczby < len(nums):
#             while zera < len(nums)-1 and nums[zera] != 0:
#                 zera += 1
#                 liczby += 1
#             while liczby < len(nums)-1 and nums[liczby] == 0:
#                 liczby += 1
            
#             pomoc = nums[zera]
#             nums[zera] = nums[liczby]
#             nums[liczby] = pomoc

#             zera += 1
#             liczby += 1



        


        