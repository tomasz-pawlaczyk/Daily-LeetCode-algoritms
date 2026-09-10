class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s)-1
        while i <= j:
            lewe = s[i].lower()
            prawe = s[j].lower()

            if not lewe.isalnum():
                i += 1
            elif not prawe.isalnum():
                j -= 1
            else:
                if lewe == prawe:
                    i += 1
                    j -= 1
                else:
                    return False
        return True

                
        