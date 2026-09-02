# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# REKURENCYJNA - moja
# class Solution:
#     def maszeruj(self, lewe, prawe, wynik):
#         if lewe is None and prawe is None:
#             return 
#         if lewe is None or prawe is None:
#             wynik[0] = False
#             return 
#         if lewe.val != prawe.val:
#             wynik[0] = False
#             return

#         self.maszeruj(lewe.left, prawe.right, wynik)
#         self.maszeruj(lewe.right, prawe.left, wynik)

#     def isSymmetric(self, root: TreeNode | None) -> bool:
#         wynik = [True]

#         self.maszeruj(root.left, root.right, wynik)
#         return wynik[0]


# REKURENCYJNA - wzorcowa
class Solution:
    def maszeruj(self, lewe, prawe):
        if lewe is None and prawe is None:
            return True
        if lewe is None or prawe is None:
            return False
        if lewe.val != prawe.val:
            return False
        return self.maszeruj(lewe.left, prawe.right) and self.maszeruj(lewe.right, prawe.left)

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.maszeruj(root.left, root.right)


# ITERACYJNA - moja
# class Solution:
#     def isSymmetric(self, root: TreeNode | None) -> bool:
#         if root is None:
#             return True
#         lewe, prawe = root.left, root.right
#         stos_lewe = []
#         stos_prawe = []
        
#         while lewe is not None or len(stos_lewe) > 0:
#             if lewe is not None:
#                 if prawe is None:
#                     return False

#                 stos_lewe.append(lewe)
#                 lewe = lewe.left
#                 stos_prawe.append(prawe)
#                 prawe = prawe.right

#             elif len(stos_lewe) > 0:
#                 if len(stos_prawe) <= 0:
#                     return False

#                 if prawe is not None:
#                     return False

#                 lewe = stos_lewe.pop()
#                 prawe = stos_prawe.pop()
#                 if lewe.val != prawe.val:
#                     return False
#                 lewe = lewe.right
#                 prawe = prawe.left

#         if lewe is None and prawe is not None:
#             return False
#         return True


# ITERACYJNA - wzorcowa na krotce
# class Solution:
#     def isSymmetric(self, root):
#         if root is None:
#             return True
#         stos = [(root.left, root.right)]
#         while stos:
#             lewe, prawe = stos.pop()
#             if lewe is None and prawe is None:
#                 continue
#             if lewe is None or prawe is None or lewe.val != prawe.val:
#                 return False
#             stos.append((lewe.left, prawe.right))
#             stos.append((lewe.right, prawe.left))
#         return True
        


# class Solution:
#     def isSymmetric(self, root: TreeNode | None) -> bool: