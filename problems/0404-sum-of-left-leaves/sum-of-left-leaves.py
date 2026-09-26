# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:

        self.suma = 0

        def przechodz(node, czy_lewy):
            if node is None:
                return 

            if node.left is None and node.right is None and czy_lewy:
                self.suma += node.val

            przechodz(node.left, True)
            przechodz(node.right, False)
        
        przechodz(root, False)
        return self.suma
