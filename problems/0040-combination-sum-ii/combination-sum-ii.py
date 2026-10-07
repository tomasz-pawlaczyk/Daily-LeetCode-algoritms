class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):                
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result



# Wersja z Counterem
# from collections import Counter

# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
#         liczniki = sorted(Counter(candidates).items())   # [(wartość, ile_razy), ...]
#         result = []

#         def backtrack(idx, remaining, path):
#             if remaining == 0:
#                 result.append(path[:])
#                 return
#             for j in range(idx, len(liczniki)):
#                 wartosc, ile = liczniki[j]
#                 if wartosc > remaining:
#                     break
#                 reszta = remaining
#                 uzyte = 0
#                 while uzyte < ile and reszta >= wartosc:
#                     path.append(wartosc)
#                     reszta -= wartosc
#                     uzyte += 1
#                     backtrack(j + 1, reszta, path)
#                 del path[len(path) - uzyte:]

#         backtrack(0, target, [])
#         return result