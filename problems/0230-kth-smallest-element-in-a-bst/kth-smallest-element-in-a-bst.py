# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        stos = []
        node = root
        count = 0

        while len(stos) > 0 or node is not None:
            if node is not None:
                stos.append(node)
                node = node.left
            else:
                node = stos.pop()

                count += 1
                if count == k:
                    return node.val

                node = node.right

# ----------
# FOLLOW-UP
# ----------

# If the BST is modified frequently and I need fast kth-smallest queries, I'd augment each node with a size field — the number of nodes in its subtree, including itself. On insert and delete, I'd update this field along the path from the root to the modified node, which costs O(h) in addition to the insert/delete itself.

# With that in place, kthSmallest no longer needs an inorder traversal. At each node, I compare k to the size of the left subtree:

# if k <= left_size, the answer is in the left subtree, so I recurse left with the same k
# if k == left_size + 1, the current node is the answer
# otherwise, the answer is in the right subtree, so I recurse right with k - left_size - 1

# This turns each query into a single root-to-leaf walk — O(h) instead of O(h+k), since I never have to visit nodes outside the direct path to the answer.

# One caveat: a plain BST can degenerate to O(n) height in the worst case, so for a real performance guarantee I'd want a self-balancing tree — AVL or red-black — which keeps h at O(log n). That would make both the updates and the queries O(log n).

# CODE ---------
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.rozmiar = 1  # rozmiar poddrzewa, wliczając siebie

# class AugmentedBST:
#     def __init__(self):
#         self.root = None

#     def insert(self, val):
#         self.root = self._insert(self.root, val)

#     def _insert(self, node, val):
#         if node is None:
#             return TreeNode(val)
#         if val < node.val:
#             node.left = self._insert(node.left, val)
#         else:
#             node.right = self._insert(node.right, val)
#         node.rozmiar = 1 + self._size(node.left) + self._size(node.right)
#         return node

#     def delete(self, val):
#         self.root = self._delete(self.root, val)

#     def _delete(self, node, val):
#         if node is None:
#             return None
#         if val < node.val:
#             node.left = self._delete(node.left, val)
#         elif val > node.val:
#             node.right = self._delete(node.right, val)
#         else:
#             if node.left is None:
#                 return node.right
#             if node.right is None:
#                 return node.left
#             nastepnik = node.right
#             while nastepnik.left is not None:
#                 nastepnik = nastepnik.left
#             node.val = nastepnik.val
#             node.right = self._delete(node.right, nastepnik.val)
#         node.rozmiar = 1 + self._size(node.left) + self._size(node.right)
#         return node

#     def _size(self, node):
#         return node.rozmiar if node is not None else 0

#     def kthSmallest(self, k):
#         node = self.root
#         while node is not None:
#             lewy_rozmiar = self._size(node.left)
#             if k <= lewy_rozmiar:
#                 node = node.left
#             elif k == lewy_rozmiar + 1:
#                 return node.val
#             else:
#                 k -= lewy_rozmiar + 1
#                 node = node.right
#         return None