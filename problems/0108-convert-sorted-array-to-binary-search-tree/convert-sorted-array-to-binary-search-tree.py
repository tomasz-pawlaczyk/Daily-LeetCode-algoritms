# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buduj(self, nums, lewo, prawo):
        dlugosc = prawo - lewo
        if dlugosc == 0:
            return None 
        
        indeks = (lewo + prawo)//2
        nowy_wezel = TreeNode(nums[indeks])
        nowy_wezel.left = self.buduj(nums, lewo, indeks)
        nowy_wezel.right = self.buduj(nums, indeks + 1, prawo)

        return nowy_wezel

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        drzewo = self.buduj(nums, 0, len(nums))
        return drzewo


