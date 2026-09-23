class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

        self.sumy = []
        suma = 0
        for i in range(len(nums)):
            suma += nums[i]
            self.sumy.append(suma)       

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumy[right]
        return self.sumy[right] - self.sumy[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)