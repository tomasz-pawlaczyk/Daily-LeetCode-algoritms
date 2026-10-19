# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        def explore(node, current_max):
            if node is None:
                return

            if node.val >= current_max:
                current_max = node.val
                self.result += 1
        
            explore(node.left, current_max)
            explore(node.right, current_max)

        explore(root, -float('inf'))
        return self.result





