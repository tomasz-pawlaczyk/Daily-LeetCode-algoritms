class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        laczny = n+m-1

        while laczny >= 0 and i >= 0 and j >= 0 : # do zmiany war konca
            if nums1[i] > nums2[j]:
                nums1[laczny] = nums1[i]
                nums1[i] = 0
                i -= 1
            else:
                nums1[laczny] = nums2[j]
                j -= 1
            laczny -= 1
            
        if m == 0 or i == -1:
            m_2 = 0
            for k in range(j+1):
                nums1[m_2] = nums2[k]
                m_2 += 1
            
            



        