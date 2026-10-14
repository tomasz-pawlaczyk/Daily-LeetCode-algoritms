class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        start, finish = 0, 0 
        max_lenght = 0
        while finish < len(s):
            if s[finish] not in unique:
                unique.add(s[finish])
                finish += 1
                if len(unique) > max_lenght:
                    max_lenght = len(unique)
            else:
                unique.remove(s[start])
                start += 1

        return max_lenght


# Wersja z możliwością przeskakiwania do miejsca, gdzie element się rzeczywiście powtarzał, zamiast chodzić +1 
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         last = {}            # znak -> indeks ostatniego wystąpienia
#         start = 0
#         max_length = 0
#         for finish, ch in enumerate(s):
#             if ch in last and last[ch] >= start:
#                 start = last[ch] + 1
#             last[ch] = finish
#             max_length = max(max_length, finish - start + 1)
#         return max_length