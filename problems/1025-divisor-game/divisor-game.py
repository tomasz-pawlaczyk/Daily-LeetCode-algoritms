class Solution:
    def divisorGame(self, n: int) -> bool:
        self.slownik = {0:False, 1:False, 2:True, 3:False} # czy pozycja wygrywa
        if n in self.slownik:
            return self.slownik[n]

        def rekurencja(n):
            i = 1
            while (i*i <= n):
                for x in {i, n // i}:
                    if n % x == 0:
                        if (n-x) not in self.slownik:
                            self.slownik[n-x] = not rekurencja(n-x)  
                        if self.slownik[n-x]:
                            return self.slownik[n-x]
                i += 1
            self.slownik[n] = False
            return False

        return rekurencja(n)


# Trik
# class Solution:
#     def divisorGame(self, n: int) -> bool:
#         return n % 2 == 0