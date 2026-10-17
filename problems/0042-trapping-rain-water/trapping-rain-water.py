class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water_sum = 0
        while left < right:
            if height[left] > max_left:
                max_left = height[left]
            if height[right] > max_right:
                max_right = height[right]
            zapora = min(max_left, max_right)

            if max_left < max_right:
                left += 1
                water_sum += max(0, zapora - height[left])
            else:
                right -= 1
                water_sum += max(0, zapora - height[right])
        return water_sum

            

        