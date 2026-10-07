# Wersja pop/append - najlepsza
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result



# Wersja czytelniejsza z przekazywaniem listy
# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         candidates.sort()
#         result = []

#         def backtrack(start, remaining, path):
#             if remaining == 0:
#                 result.append(path)
#                 return
#             for i in range(start, len(candidates)):
#                 if candidates[i] > remaining:
#                     break
#                 backtrack(i, remaining - candidates[i], path + [candidates[i]])

#         backtrack(0, target, [])
#         return result




# Moje poprawione
# class Solution:
    # def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]
    #     self.result = []
        # def backtracking(kandydat, candidates, target, obecni):
        #     target -= kandydat
        #     if target == 0:
        #         self.result.append(obecni)
        #         return
        #     elif target < 0:
        #         return
        #     for number in candidates:
        #         if number >= kandydat:
        #             backtracking(number, candidates, target, obecni + [number])
#         backtracking(0, candidates, target, [])
#         return self.result


# Moje pierwsze
# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         self.result = []

#         def backtracking(kandydat, candidates, target, obecni):
#             print(kandydat, candidates, target, obecni)
#             if target == kandydat:
#                 self.result.append(obecni)
#                 return 
#             elif target < kandydat:
#                 return
            
#             for number in candidates:
#                 if number >= kandydat:
#                     backtracking(number, candidates, target-kandydat, obecni + [number])
#         backtracking(0, candidates, target, [])
#         return self.result