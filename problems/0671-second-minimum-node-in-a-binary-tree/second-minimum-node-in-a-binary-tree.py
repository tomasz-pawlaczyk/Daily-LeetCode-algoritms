# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        if root is None:
            return -1

        self.pierwszy_minimum = root.val
        self.drugi_minimum = float('inf')

        def przechodz(node):
            if node is None:
                return 
            
            if node.val < self.drugi_minimum and node.val != self.pierwszy_minimum:
                self.drugi_minimum = node.val
            
            przechodz(node.left)
            przechodz(node.right)

        przechodz(root)
        if self.drugi_minimum == float('inf'):
            return -1
        return self.drugi_minimum





        