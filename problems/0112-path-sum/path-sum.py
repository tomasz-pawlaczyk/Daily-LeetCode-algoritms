# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# REKURENCYJNIE
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        if root.left == None and root.right == None: 
            return root.val == targetSum
        
        pozostalo = targetSum - root.val
        return self.hasPathSum(root.left, pozostalo) or self.hasPathSum(root.right, pozostalo)



# ITERACYJNIE
# class Solution:
#     def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
#         if root is None:
#             return False
#         stos = [(root, root.val)]

#         while len(stos) > 0:
#             (node, suma) = stos.pop()

#             if node.left is None and node.right is None:
#                 if suma == targetSum:
#                     return True
#             if node.left is not None:
#                 stos.append((node.left, suma + node.left.val))
#             if node.right is not None:
#                 stos.append((node.right, suma + node.right.val))
         
#         return False