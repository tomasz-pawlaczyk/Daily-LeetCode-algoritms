# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        
        self.result = False
        def check(node, subNode):
            if node is None and subNode is None:
                return True
            elif node is None and subNode is not None:
                return False
            elif node is not None and subNode is None:
                return False

            if node.val != subNode.val:
                return False
            return check(node.left, subNode.left) and check(node.right, subNode.right)
           

        def iteruj(node):
            if node is None:
                return False
            
            biezace = check(node, subRoot)
            self.result = biezace or self.result
            iteruj(node.left)
            iteruj(node.right)

        iteruj(root)

        return self.result


# Wersja wzorcowa
# class Solution:
#     def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
#         def same(a, b):
#             if a is None and b is None:
#                 return True
#             if a is None or b is None:
#                 return False
#             return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
        
#         def dfs(node):
#             if node is None:
#                 return False
#             if same(node, subRoot):
#                 return True
#             return dfs(node.left) or dfs(node.right)
        
#         return dfs(root)