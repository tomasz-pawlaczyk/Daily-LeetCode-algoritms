class Solution:
    def minRotations(self, s: str) -> int:
        result = 0
        source = 0
        for letter in s:
            target = int(letter)
            steps = min(abs(target-source), 10-abs(source-target))
            result += steps
            source = target
        return result




        
        