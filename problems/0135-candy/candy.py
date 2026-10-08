class Solution:
    def candy(self, ratings: list[int]) -> int:
        cukierki = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                cukierki[i] = cukierki[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and cukierki[i] <= cukierki[i+1]:
                cukierki[i] = cukierki[i+1] + 1
        return sum(cukierki)
        



# Stała pamięć
# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         suma = 1          # pierwsze dziecko dostaje 1
#         wzrost = 0        # ile kroków w górę z rzędu
#         spadek = 0        # ile kroków w dół z rzędu
#         szczyt = 0        # długość ostatniego wzrostu (zapamiętana na czas spadku)

#         for i in range(1, len(ratings)):
#             if ratings[i] > ratings[i-1]:
#                 wzrost += 1
#                 szczyt = wzrost
#                 spadek = 0
#                 suma += 1 + wzrost
#             elif ratings[i] == ratings[i-1]:
#                 wzrost = spadek = szczyt = 0
#                 suma += 1
#             else:
#                 wzrost = 0
#                 spadek += 1
#                 suma += spadek
#                 if szczyt < spadek:
#                     suma += 1
#         return suma