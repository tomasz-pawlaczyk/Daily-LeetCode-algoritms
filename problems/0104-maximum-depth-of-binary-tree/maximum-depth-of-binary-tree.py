# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ITERACJA
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        stos = [(root, 1)]
        max_glebokosc = 0
        while len(stos) > 0:
            (node, glebokosc) = stos.pop()
            if glebokosc > max_glebokosc:
                max_glebokosc = glebokosc
            if node.left is not None:
                stos.append((node.left, glebokosc+1))
            if node.right is not None:
                stos.append((node.right, glebokosc+1))
        return max_glebokosc


        
# REKURENCJA
# class Solution:
#     def maxDepth(self, root: TreeNode | None) -> int:
        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))