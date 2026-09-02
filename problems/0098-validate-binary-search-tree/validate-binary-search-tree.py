# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        stos = []
        poprzednie = float('-inf')
        node = root

        while len(stos) > 0 or node is not None:
            if node is not None:
                stos.append(node)
                node = node.left

            else:
                node = stos.pop()
                if poprzednie >= node.val:
                    return False
                poprzednie = node.val
                node = node.right

        return True


        