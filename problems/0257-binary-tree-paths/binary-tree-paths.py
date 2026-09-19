# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root == None:
            return []

        self.biezace = []
        self.wyniki = []
        
        def explore(node):
            if node is None:
                return 
            
            self.biezace.append(node.val)
            if node.left is None and node.right is None:
                (self.wyniki).append("->".join(str(x) for x in self.biezace))
                self.biezace.pop()
                return

            explore(node.left)
            explore(node.right)
            
            self.biezace.pop()

        explore(root)
        return self.wyniki