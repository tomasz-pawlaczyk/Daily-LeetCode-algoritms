# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        lewo, prawo = 1, n
        while lewo <= prawo:
            srodek = (lewo + prawo) // 2

            if isBadVersion(srodek):
                prawo = srodek - 1
            else:
                lewo = srodek + 1
        return lewo
