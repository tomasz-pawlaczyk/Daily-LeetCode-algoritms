class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        lewo = 0
        prawo = len(nums)-1
        mid = 0

        while lewo <= prawo:
            mid = (lewo+prawo) // 2

            if target > nums[mid]:
                lewo = mid + 1
            elif target < nums[mid]:
                prawo = mid - 1
            else:
                return mid

        # if target > nums[mid]:
        #     return mid+1
        # return mid
        return lewo
        
        