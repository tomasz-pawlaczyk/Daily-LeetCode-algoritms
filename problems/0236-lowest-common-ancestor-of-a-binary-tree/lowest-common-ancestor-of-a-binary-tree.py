# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.result = None

        def DFS(node, p, q):
            if node is None:
                return 0
            
            lewe = DFS(node.left, p, q)
            prawe = DFS(node.right, p, q)
            czy_to_ja = 1 if (node.val == p or node.val == q) else 0
            suma = lewe + prawe + czy_to_ja
            print(node.val, lewe, prawe, suma)
            if suma == 2:
                self.result = node
                return 0
            else:
                return suma

        DFS(root, p.val, q.val)
        return self.result


# Czysta rekurencja
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if root is None or root.val == p.val or root.val == q.val:
#             return root
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
#         if left and right:
#             return root
#         return left or right




