class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        slownik = {}
        for i in range(len(nums)):
            potrzebna = target - nums[i]
            if potrzebna in slownik:
                return [slownik[potrzebna], i]
            
            slownik[nums[i]] = i
        


        