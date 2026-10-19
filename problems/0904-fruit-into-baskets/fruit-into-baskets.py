class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) == 1:
            return 1
        slow, fast = 0, 1
        used = [[fruits[0], 0], [None, -1]]
        result = 1
        
        while fast < len(fruits):
            if fruits[fast] == used[0][0]:
                used[0][1] = fast
                fast += 1
            elif fruits[fast] == used[1][0]:
                used[1][1] = fast 
                fast += 1
            else:
                if used[0][1] < used[1][1]:
                    slow = used[0][1] + 1
                    used[0] = [fruits[fast], fast]

                else:
                    slow = used[1][1] + 1
                    used[1] = [fruits[fast], fast]

            if result < fast - slow:
                result = fast - slow

        return result




from collections import defaultdict

# class Solution:
#     def totalFruit(self, fruits: list[int]) -> int:
#         counts = defaultdict(int)      # typ owocu -> ile razy występuje w oknie
#         left = 0
#         result = 0

#         for right, fruit in enumerate(fruits):
#             counts[fruit] += 1

#             while len(counts) > 2:     # w oknie jest za dużo typów: zwężamy od lewej
#                 counts[fruits[left]] -= 1
#                 if counts[fruits[left]] == 0:
#                     del counts[fruits[left]]
#                 left += 1

#             result = max(result, right - left + 1)

#         return result

                