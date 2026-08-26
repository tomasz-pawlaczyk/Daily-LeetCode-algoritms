class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = -1

        for fast in range(0, len(nums)):
            if nums[fast] != val:
                slow += 1
                if slow != fast:
                    nums[slow] = nums[fast]

        return slow+1
        