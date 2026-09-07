# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        self.backtracking = []
        self.suma = 0
        self.result = []

        def explore(node):
            if node is None:
                return 
            
            self.backtracking.append(node.val)
            self.suma += node.val            

            if node.left is None and node.right is None and self.suma == targetSum:
                self.result.append(list(self.backtracking))
            
            explore(node.left)
            explore(node.right)
            self.suma -= self.backtracking.pop()
            
        explore(root)
        return self.result

