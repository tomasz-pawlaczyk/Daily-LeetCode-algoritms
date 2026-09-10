# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.backtracking = 0
        self.wynik = 0

        def explore(node):
            if node is None:
                return
            self.backtracking = self.backtracking * 10 + node.val

            if node.left is None and node.right is None:
                self.wynik += self.backtracking
            
            explore(node.left)
            explore(node.right)
            self.backtracking //= 10
            
        explore(root)
        return self.wynik    
