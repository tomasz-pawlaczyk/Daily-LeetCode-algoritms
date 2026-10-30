# zwiększenie wszystkich elementów poza jednym o 1 jest równoważne, pod względem różnic między elementami, zmniejszeniu tego pominiętego elementu o 1

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nadmiar = 0
        minimum = min(nums)
        for num in nums:
            nadmiar += num - minimum
        
        return nadmiar

        