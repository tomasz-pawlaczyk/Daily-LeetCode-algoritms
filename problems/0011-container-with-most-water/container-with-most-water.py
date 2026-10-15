class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        pole_max = 0

        while left < right:
            shorter = min(height[left], height[right])
            nowe_pole = shorter * (right - left)
            if nowe_pole > pole_max:
                pole_max = nowe_pole
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return pole_max
            

        