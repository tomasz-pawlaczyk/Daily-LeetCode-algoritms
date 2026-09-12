# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# REKURENCYJNIE - nowa funkcja
# class Solution:
#     def maszeruj(self, root, wyniki):
#         if root is None:
#             return 
#         wyniki.append(root.val)
#         self.maszeruj(root.left, wyniki)
#         self.maszeruj(root.right, wyniki)

#     def preorderTraversal(self, root: TreeNode | None) -> list[int]:
#         wyniki = []
#         self.maszeruj(root, wyniki)
#         return wyniki


# REKURENCYJNIE - na starej funkcji
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# ITERACYJNIE 
# class Solution:
#     def preorderTraversal(self, root: TreeNode | None) -> list[int]:
#         stos = []
#         node = root
#         wyniki = []

#         while len(stos) > 0 or node is not None:
#             if node is not None:
#                 wyniki.append(node.val)
#                 if node.right is not None:
#                     stos.append(node.right)
#                 node = node.left
#             else:
#                 node = stos.pop()
#         return wyniki
