class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        greed, size = 0, 0
        result = 0
        while size < len(s) and greed < len(g):
            if g[greed] <= s[size]:
                greed += 1
                size += 1
                result += 1
            else:
                size += 1
        return result
            
        