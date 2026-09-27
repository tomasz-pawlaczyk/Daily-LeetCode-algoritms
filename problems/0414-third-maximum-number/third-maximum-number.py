class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = -float('inf')
        max2 = -float('inf')
        max3 = -float('inf')
        for num in nums:
            if num > max1:
                pom = max1
                max1 = num
                max3 = max2
                max2 = pom
            elif num == max1:
                continue
            elif num > max2:
                pom = max2
                max2 = num
                max3 = pom
            elif num == max2:
                continue
            elif num > max3:
                max3 = num
        
        if max3 != -float('inf'):
            return max3
        return max1
        