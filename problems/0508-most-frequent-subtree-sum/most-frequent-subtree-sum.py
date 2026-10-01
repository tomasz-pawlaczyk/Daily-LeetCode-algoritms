# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        self.sums = {}

        def explore(node):
            if node is None:
                return 0

            lewe = explore(node.left)
            prawe = explore(node.right)
            suma = node.val + lewe + prawe
            self.sums[suma] = self.sums.get(suma, 0) + 1

            return suma 
            

        explore(root)
        maks_wartosc = max(self.sums.values())
        najczestsze = [klucz for klucz, wartosc in self.sums.items() if wartosc == maks_wartosc]

        return najczestsze



