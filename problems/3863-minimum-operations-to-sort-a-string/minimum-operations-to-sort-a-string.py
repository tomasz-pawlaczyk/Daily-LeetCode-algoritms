class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0                    
        if n == 2:
            return -1   

        lo, hi = min(s), max(s)
        if s[0] == lo or s[-1] == hi:
            return 1                     
        if s.find(lo) != n - 1 or s.rfind(hi) != 0:
            return 2                      
        return 3

# Dlaczego te przypadki:
# 0: napis już jest posortowany.
# -1: dla n = 2 dozwolone są tylko kawałki długości 1, a ich sortowanie nic nie zmienia. Nieposortowanego napisu o długości 2 nie da się naprawić. Dla n ≥ 3 zawsze istnieje rozwiązanie.
# 1: jeśli s[0] jest najmniejszym znakiem, wystarczy posortować s[1:]. Jeśli s[-1] jest największym, wystarczy posortować s[:-1]. Każdy z tych kawałków jest właściwy, bo nie obejmuje całego napisu.
# 2: gdy min leży gdzieś przed końcem (istnieje jego wystąpienie na pozycji < n-1), sortujesz s[:-1] (min trafia na początek), a potem s[1:] (reszta układa się w całość). Symetrycznie, gdy max leży gdzieś za początkiem: najpierw s[1:] (max trafia na koniec), potem s[:-1].
# 3: zostaje przypadek, gdy min jest wyłącznie na końcu, a max wyłącznie na początku. Dwa ruchy nie wystarczą, ale trzy zawsze tak (przykład cba: cb, potem ca, potem ba).




# class Solution:
#     def minOperations(self, s: str) -> int:
#         mini, maxi = min(s), max(s)
#         last_max, first_min = 0, float('inf')
#         for i in range(len(s)):
#             if s[i] == maxi:
#                 last_max = max(last_max, i)
#             elif s[i] == mini:
#                 first_min = min(first_min, i)

#         is_sorted = True
#         for i in range(len(s) - 1):
#             if s[i] > s[i + 1]:
#                 is_sorted = False
#                 break

#         if is_sorted:
#             return 0
#         elif len(s) <= 2:
#             return -1
#         elif mini == s[0] or maxi == s[-1]:
#             return 1
#         elif first_min != len(s) - 1 or last_max != 0:
#             return 2
#         else:
#             return 3