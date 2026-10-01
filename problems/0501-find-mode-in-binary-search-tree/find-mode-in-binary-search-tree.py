# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# ITERACYJNA - moja
# class Solution:
#     def findMode(self, root: TreeNode | None) -> list[int]:
#         if root is None:
#             return []

#         stos = []
#         ilosc = 0
#         node = root
#         dominanty = []
#         ilosc_dominanty = 0
#         poprzednie = None
#         while stos or node is not None:
#             if node is not None:
#                 stos.append(node)
#                 node = node.left
#             else:
#                 node = stos.pop()
                
#                 if node.val == poprzednie:
#                     ilosc += 1
#                 else:
#                     ilosc = 1
#                 if ilosc > ilosc_dominanty:
#                     ilosc_dominanty = ilosc
#                     dominanty = [node.val]
#                 elif ilosc == ilosc_dominanty:
#                     dominanty.append(node.val)
#                 poprzednie = node.val
#                 node = node.right

#         return dominanty


# REKURENCYJNA 
# class Solution:
#     def findMode(self, root: TreeNode | None) -> list[int]:
#         self.poprzedni = None
#         self.ilosc = 0
#         self.ilosc_max = 0
#         self.dominanty = []

#         def inorder(node):
#             if node is None:
#                 return
#             inorder(node.left)

#             if node.val == self.poprzedni:
#                 self.ilosc += 1
#             else:
#                 self.ilosc = 1
#             if self.ilosc > self.ilosc_max:
#                 self.ilosc_max = self.ilosc
#                 self.dominanty = [node.val]
#             elif self.ilosc == self.ilosc_max:
#                 self.dominanty.append(node.val)
#             self.poprzedni = node.val

#             inorder(node.right)

#         inorder(root)
#         return self.dominanty 


# Wersja Morris-traversal

class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        poprzednie = None
        ilosc = 0
        ilosc_dominanty = 0
        dominanty = []

        node = root
        while node is not None:
            if node.left is None:
                # przetwórz node
                if node.val == poprzednie:
                    ilosc += 1
                else:
                    ilosc = 1
                if ilosc > ilosc_dominanty:
                    ilosc_dominanty = ilosc
                    dominanty = [node.val]
                elif ilosc == ilosc_dominanty:
                    dominanty.append(node.val)
                poprzednie = node.val
                node = node.right
            else:
                pred = node.left
                while pred.right is not None and pred.right is not node:
                    pred = pred.right

                if pred.right is None:
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None  # usuń nić, przywróć drzewo
                    # przetwórz node (druga wizyta)
                    if node.val == poprzednie:
                        ilosc += 1
                    else:
                        ilosc = 1
                    if ilosc > ilosc_dominanty:
                        ilosc_dominanty = ilosc
                        dominanty = [node.val]
                    elif ilosc == ilosc_dominanty:
                        dominanty.append(node.val)
                    poprzednie = node.val
                    node = node.right

        return dominanty

        