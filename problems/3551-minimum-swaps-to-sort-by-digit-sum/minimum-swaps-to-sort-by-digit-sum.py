class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        sums = []
        for num in nums:
            suma = 0
            while num > 0:
                suma += num % 10 
                num //= 10
            sums.append(suma)

        n = len(nums)
        order = sorted(range(n), key=lambda i: (sums[i], nums[i]))
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] is True or order[i] == i:
                continue
            
            lenght = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = order[j]
                lenght += 1
            
            swaps += lenght-1
        return swaps
            









# Moje - za wolne
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         sums = []
#         for num in nums:
#             suma = 0
#             while num > 0:
#                 suma += num % 10 
#                 num //= 10
#             sums.append(suma)

#         counter = 0
#         for i in range(len(nums) - 1):
#             k = i
#             for j in range(i + 1, len(nums)):
#                 if (sums[j], nums[j]) < (sums[k], nums[k]):
#                     k = j
#             if k != i:
#                 sums[i], sums[k] = sums[k], sums[i]
#                 nums[i], nums[k] = nums[k], nums[i]
#                 counter += 1
#         return counter


        