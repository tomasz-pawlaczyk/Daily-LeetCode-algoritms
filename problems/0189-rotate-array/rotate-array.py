
# Najprostsze O(n), O(n)
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n = len(nums)
#         result = [0] * n
#         for i in range(n):
#             result[(i + k) % n] = nums[i]
#         nums[:] = result



# Trzy odwrócenia O(n), O(1)
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n = len(nums)
#         k %= n

#         def reverse(l: int, r: int) -> None:
#             while l < r:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 l += 1
#                 r -= 1

#         reverse(0, n - 1)    # odwróć całość
#         reverse(0, k - 1)    # odwróć pierwsze k
#         reverse(k, n - 1)    # odwróć resztę



# Rozwiązanie ze skakaniem o 'k' elementów
# algorytm żonglujący O(n), O(1)
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return

        start = 0  # indeks początku bieżącego cyklu
        i = 0
        visited = 0  # ile elementów już leży na swoim miejscu
        current = nums[0]

        while visited < n:
            new_i = (i + k) % n
            # połóż current, weź to, co tam leżało
            nums[new_i], current = current, nums[new_i]  
            i = new_i
            visited += 1

            if i == start and visited < n:  # cykl domknięty, a coś jeszcze zostało
                start += 1
                i = start
                current = nums[i]