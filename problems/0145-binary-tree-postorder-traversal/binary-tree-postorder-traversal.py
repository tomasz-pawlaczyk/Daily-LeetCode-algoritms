# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# REKURENCYJNIE - 1 funkcja
# class Solution:
#     def postorderTraversal(self, root: TreeNode | None) -> list[int]:
#         if root is None:
#             return []
#         return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        

# REKURENCYJNIE - 2 funkcje
# class Solution:
#     def maszeruj(self, root, wyniki):
#         if root is None:
#             return 
#         self.maszeruj(root.left, wyniki)
#         self.maszeruj(root.right, wyniki)
#         wyniki.append(root.val)

#     def postorderTraversal(self, root: TreeNode | None) -> list[int]:
#         wyniki = []
#         self.maszeruj(root, wyniki)
#         return wyniki

# ITERACYJNIE
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        stos = []
        wyniki = []
        node = root
        ostatnio_odwiedzony = None
        while node is not None or len(stos) > 0:
            if node is not None:
                stos.append(node)
                node = node.left
            else:                
                szczyt = stos[-1]
                if szczyt.right is not None and szczyt.right is not ostatnio_odwiedzony:
                    node = szczyt.right
                else:
                    wyniki.append(szczyt.val)
                    ostatnio_odwiedzony = stos.pop()
        return wyniki
