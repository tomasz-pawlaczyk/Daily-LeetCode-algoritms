class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)

        # I. Usuwamy spacje
        k = 0
        for i in range(0, n-1):
            if s[i] != ' ' or (s[i+1] != ' ' and k>0):
                s[k] = s[i]
                k += 1

        if s[n-1] != ' ':
            s[k] = s[n-1]
            k += 1
        del s[k:]
        print(s)
            
        # Mamy wyczyszczone spacje
        # II. Odwracamy wszystko
        # s = lista_bez_spacji
        n = len(s)
        left, right = 0, n-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

        # III. Odwracamy same słowa
        fast, slow = 0, 0 
        word_end = 0
        while fast < n: 
            while fast+1 < n and s[fast+1] != ' ':
                fast += 1
            word_end = fast
            while slow < fast:
                s[slow], s[fast] = s[fast], s[slow]
                slow += 1
                fast -= 1
            if word_end == n-1:
                break
            slow, fast = word_end+2, word_end+2
        print(s)
        return "".join(s)



        
# Pythonowe sztuczki
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(reversed(s.split()))
