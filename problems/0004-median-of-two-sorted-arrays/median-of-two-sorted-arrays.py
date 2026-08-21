class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # nie ma chuja ze sam bym na to wpadł  
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        lewo, prawo = 0, m

        while lewo <= prawo:
            partitionX = (lewo + prawo) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 1:
                    return float(max(maxLeftX, maxLeftY))
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            elif maxLeftX > minRightY:
                prawo = partitionX - 1
            else:
                lewo = partitionX + 1




# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

#         i = 0
#         j = 0
#         n, m = len(nums1), len(nums2)
#         poprzednie, aktualne = None, None
        
#         while (i+j) <= (n+m)//2 :
#             poprzednie = aktualne   

#             if i != n and (j == m or nums1[i] < nums2[j]):
#                 aktualne = nums1[i]
#                 i += 1

#             else:
#                 aktualne = nums2[j]
#                 j += 1

#         if (n+m)%2 == 1:
#             return float(aktualne)
#         else:
#             return (poprzednie+aktualne)/2
        