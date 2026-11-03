# Stała pamięć
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        A = edges[0][0]
        B = edges[0][1]
        if A in edges[1]:
            return A
        else:
            return B


# O(n) szybkości i pamięci
# class Solution:
#     def findCenter(self, edges: list[list[int]]) -> int:
#         neighbours = {}
#         for item in edges:
#             A = item[0]
#             B = item[1]
#             neighbours[A] = neighbours.get(A, 0) + 1
#             neighbours[B] = neighbours.get(B, 0) + 1

#         n = len(neighbours)

#         for i in range(1, n + 1):
#             if neighbours[i] == n-1:
#                 return i

        