class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        liczba = None
        licznik = 0
        for num in nums:
            if licznik == 0:
                liczba = num
            
            if num == liczba:
                licznik += 1
            else:
                licznik -= 1
        return liczba
        

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         slownik = {}
#         for num in nums:
#             if num in slownik:
#                 slownik[num] += 1
#             else:
#                 slownik[num] = 1
        
#         wynik = sorted(slownik.items(), key = lambda x:-x[1])
#         return wynik[0][0]
        
        