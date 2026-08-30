class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, -1, -1):
            current = digits[i]
            increment = current + 1
            reszta = increment % 10

            if reszta != 0:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                return digits

        