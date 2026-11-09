class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        nums = list(sorted(set(nums)))
        oczekiwana = lower
        wyniki = []

        for num in nums:
            if num < lower:
                continue
            elif num > upper:
                break

            if num > oczekiwana:
                wyniki.append([oczekiwana, num-1])
                oczekiwana = num + 1           
            if num == oczekiwana:
                oczekiwana += 1
        # koniec pętli

        if oczekiwana <= upper:
            wyniki.append([oczekiwana, upper])

        return wyniki






# class Solution:
#     def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

#         zbior = list(set(nums))
#         brakujace = set([i for i in range(lower, upper+1)])
#         for num in zbior:
#             brakujace.discard(num)
#         brakujace = sorted(list(brakujace))
 
        
#         n = len(brakujace)
#         if n == 0:
#             return []
        
#         start = None
#         finish = None
#         poprzednie = None
#         wyniki = []
#         for i in range(n):
#             cyfra = brakujace[i]
#             # potencjalnie niepotrzebny warunek bo można zrobić przed forem ze start = brakujace[0]
#             if start is None:
#                 start = cyfra
#                 poprzednie = cyfra

#             else:
#                 if cyfra == poprzednie + 1:
#                     poprzednie = cyfra
#                 elif cyfra != poprzednie:
#                         finish = poprzednie
#                         wyniki.append([start, finish])
#                         finish = None
#                         start = cyfra
#                         poprzednie = cyfra

#         if poprzednie == start:
#             wyniki.append([start, start])
#         else:
#             wyniki.append([start, poprzednie])

            
#         return wyniki


        
        