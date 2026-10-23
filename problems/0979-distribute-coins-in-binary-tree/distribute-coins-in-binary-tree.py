# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# wersja ogólna z zadania
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        self.movements = 0

        def explore(node):
            if node is None:
                return 0
            lewe = explore(node.left)
            prawe = explore(node.right)
            self.movements += abs(lewe) + abs(prawe)
            return node.val - 1 + lewe + prawe

        explore(root)
        return self.movements

# Moja wersja działająca w ogólności
# class Solution:
#     def distributeCoins(self, root: TreeNode | None) -> int:
#         self.coin_number = 0
#         self.node_number = 0

#         def count_sums(node):
#             if node is None:
#                 return
#             self.node_number += 1
#             self.coin_number += node.val
#             count_sums(node.left)
#             count_sums(node.right)
#         count_sums(root)

#         self.correct_number = self.coin_number // self.node_number
#         self.movements = 0

#         def explore(node):
#             if node is None:
#                 return 0

#             current_bilans = (node.val - self.correct_number)
#             lewe = explore(node.left)
#             prawe = explore(node.right)

#             self.movements += abs(lewe) + abs(prawe)
#             return current_bilans + lewe + prawe

#         nadwyzka = explore(root)
#         return self.movements
