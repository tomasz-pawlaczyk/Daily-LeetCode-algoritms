# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        kolejka = deque([(root, 1)])

        while len(kolejka) > 0:
            (node, glebokosc) = kolejka.popleft()

            if node.left is None and node.right is None:
                return glebokosc
            if node.left is not None:
                kolejka.append((node.left, glebokosc+1))
            if node.right is not None:
                kolejka.append((node.right, glebokosc+1))

        return min_glebokosc




# REKURENCJA DFS
# class Solution:
#     def rekurencja(self, node):
#         if node is None:
#             return float('inf')
#         if node.left is None and node.right is None:
#             return 1
        
#         return 1 + min(self.rekurencja(node.left), self.rekurencja(node.right))

#     def minDepth(self, root):
#         if root is None:
#             return 0
        
#         return self.rekurencja(root)



# ITERACYJNE DFS
# class Solution:
#     def minDepth(self, root: TreeNode | None) -> int:
#         if root is None:
#             return 0
#         stos = [(root, 1)]
#         min_glebokosc = float('inf')
#         while len(stos) > 0:
#             (node, glebokosc) = stos.pop()
#             if node.left is None and node.right is None and glebokosc < min_glebokosc:
#                 min_glebokosc = glebokosc
#             if node.left is not None:
#                 stos.append((node.left, glebokosc + 1))
#             if node.right is not None:
#                 stos.append((node.right, glebokosc + 1)) 
#         return min_glebokosc