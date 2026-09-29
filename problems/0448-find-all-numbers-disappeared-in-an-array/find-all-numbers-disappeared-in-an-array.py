class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            wartosc = nums[i]

            nums[abs(wartosc)-1] = -abs(nums[abs(wartosc)-1])

        wynik = []
        for i in range(len(nums)):
            if nums[i] > 0:
                wynik.append(i+1)

        return wynik




# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             wartosc = nums[i]

#             while wartosc != None:
#                 zapamietaj = nums[wartosc-1]
#                 nums[wartosc-1] = None
#                 wartosc = zapamietaj

#         wynik = []
#         for i in range(len(nums)):
#             if nums[i] != None:
#                 wynik.append(i+1)

#         return wynik
