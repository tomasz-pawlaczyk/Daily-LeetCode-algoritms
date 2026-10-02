# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0    # wartość globalna! 

        def zmierz_dlugosc(node):
            if node is None:
                return 0

            lewy = zmierz_dlugosc(node.left)
            prawy = zmierz_dlugosc(node.right)
            aktualny_diameter = lewy + prawy

            if self.diameter < aktualny_diameter:
                self.diameter = aktualny_diameter

            return 1 + max(lewy, prawy)
        
        zmierz_dlugosc(root)
        return self.diameter




