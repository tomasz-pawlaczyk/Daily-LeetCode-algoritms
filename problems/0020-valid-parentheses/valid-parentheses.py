class Solution:
    def isValid(self, s: str) -> bool:
        stos = []
        pary = {')': '(', ']': '[', '}': '{'}
        for znak in s:
            if znak in '([{':
                stos.append(znak)
            else:
                if not stos or stos.pop() != pary[znak]:
                    return False
        return not stos
        

# MOJE
# class Solution:
#     def isValid(self, s: str) -> bool:
#         oczekiwane_zamkniecie = []

#         for znak in s:
#             if znak == '(':
#                 oczekiwane_zamkniecie.append(')')
#             elif znak == ')':
#                 if len(oczekiwane_zamkniecie) <= 0:
#                     return False
#                 if oczekiwane_zamkniecie.pop() != znak:
#                     return False

#             elif znak == '{':
#                 oczekiwane_zamkniecie.append('}')
#             elif znak == '}':
#                 if len(oczekiwane_zamkniecie) <= 0:
#                     return False
#                 if oczekiwane_zamkniecie.pop() != znak:
#                     return False

#             elif znak == '[':
#                 oczekiwane_zamkniecie.append(']')
#             elif znak == ']':
#                 if len(oczekiwane_zamkniecie) <= 0:
#                     return False
#                 if oczekiwane_zamkniecie.pop() != znak:
#                     return False 
#         if len(oczekiwane_zamkniecie) != 0:
#             return False
#         return True
