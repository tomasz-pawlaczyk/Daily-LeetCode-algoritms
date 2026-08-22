class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        odwrocona_polowa = 0
        while x > odwrocona_polowa:
            odwrocona_polowa = odwrocona_polowa * 10 + x % 10
            x //= 10

        return x == odwrocona_polowa or x == odwrocona_polowa // 10


# class Solution:
#     def isPalindrome(self, x: int) -> bool:

#         if x < 0:
#             return False
#         elif x <= 9:
#             return True
        
#         kopia = x
#         proba = 0
#         while kopia > 0:
#             reszta = kopia % 10
#             proba = proba*10 + reszta
#             kopia //= 10
#         if x == proba:
#             return True
#         return False
