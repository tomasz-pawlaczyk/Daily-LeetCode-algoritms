class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lista1 = set(nums1)
        lista2 = set(nums2)
        return list(lista1 & lista2)

        