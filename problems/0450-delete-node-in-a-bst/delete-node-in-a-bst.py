# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            nastepnik = root.right
            while nastepnik.left is not None:
                nastepnik = nastepnik.left
            root.val = nastepnik.val
            root.right = self.deleteNode(root.right, nastepnik.val)
        return root



# Moje
# class Solution:
#     def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
#         node = root
#         if node is None:
#             return None
#         if node.val == key:
#             if node.left is None and node.right is None:
#                 return None
#             elif node.right is None:
#                 return node.left
#         poprzedni_lewy = None
#         poprzedni_prawy = None
        
#         while node is not None:
#             if key < node.val:
#                 poprzedni_lewy = node
#                 poprzedni_prawy = None
#                 node = node.left 
#             elif key > node.val:
#                 poprzedni_prawy = node
#                 poprzedni_lewy = None
#                 node = node.right
#             else:
#                 # node - nasz
#                 if node.left is None and node.right is None:
#                     if poprzedni_lewy is not None:
#                         poprzedni_lewy.left = None
#                     else:
#                         poprzedni_prawy.right = None
#                     break

#                 elif node.right is None:
#                     if poprzedni_lewy is not None:
#                         poprzedni_lewy.left = node.left
#                     else:
#                         poprzedni_prawy.right = node.left
#                     break
#                 else:
#                     glowny_wezel = node
#                     poprzednik = node
#                     node = node.right

#                     while node.left is not None:
#                         poprzednik = node
#                         node = node.left
                    
#                     if poprzedni_lewy is not None:
#                         poprzedni_lewy.left = node
#                     elif poprzedni_prawy is not None:
#                         poprzedni_prawy.right = node
#                     else:
#                         root = node
                    
#                     node.left = glowny_wezel.left
#                     if poprzednik != glowny_wezel:
#                         poprzednik.left = node.right
#                         node.right = glowny_wezel.right
#                     break

#         return root


