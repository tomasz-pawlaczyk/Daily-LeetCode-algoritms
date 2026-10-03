# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# REKURENCYJNE
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.suma_tiltow = 0
        
        def suma_poddrzewa(node):
            if node is None:
                return 0
            lewa = suma_poddrzewa(node.left)
            prawa = suma_poddrzewa(node.right)
            self.suma_tiltow += abs(lewa - prawa)
            return node.val + lewa + prawa
        
        suma_poddrzewa(root)
        return self.suma_tiltow


        