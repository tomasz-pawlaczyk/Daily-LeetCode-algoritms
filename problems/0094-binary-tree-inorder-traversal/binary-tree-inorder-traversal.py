# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# WERSJA REKURENCYJNA
# class Solution:
#     def maszeruj(self, node, wynik):
#         if node is None:
#             return
        
#         self.maszeruj(node.left, wynik)
#         wynik.append(node.val)
#         self.maszeruj(node.right, wynik)

#     def inorderTraversal(self, root: TreeNode | None) -> list[int]:
#         wynik = []
#         self.maszeruj(root, wynik)
#         return wynik


# WERSJA ITERACYJNA
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        stos = []
        node = root
        wyniki = []
        while node is not None or len(stos) > 0:
            if node is not None:
                stos.append(node)
                node = node.left

            else:
                node = stos.pop()
                wyniki.append(node.val)
                node = node.right

        return wyniki