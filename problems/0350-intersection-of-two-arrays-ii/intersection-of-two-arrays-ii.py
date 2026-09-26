from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        wynik = []
        for key in counter1.keys():
            if key in counter2.keys():
                for _ in range((min(counter1[key], counter2[key]))):
                    wynik.append(key)
        return wynik


# FOLLOW-UP 1
# def intersect_sorted(nums1, nums2):
#     nums1.sort()
#     nums2.sort()
#     i, j = 0, 0
#     wynik = []
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             i += 1
#         elif nums1[i] > nums2[j]:
#             j += 1
#         else:
#             wynik.append(nums1[i])
#             i += 1
#             j += 1
#     return wynik


# FOLLOW-UP 2
# def intersect_small_nums1(nums1, nums2):
#     counter1 = Counter(nums1)
#     wynik = []
#     for num in nums2:
#         if counter1[num] > 0:
#             wynik.append(num)
#             counter1[num] -= 1
#     return wynik


# FOLLOW-UP 3
# Robimy tak jak w follow-up 2 czyli Counter dla małego, lista dla dużego. 
# Natomiast z dysku przesyłamy dużą listę po częściach

# def intersect_streamed(nums1, plik_nums2, rozmiar_fragmentu=1000):
#     counter1 = Counter(nums1)
#     wynik = []
#     fragment = []
#     with open(plik_nums2) as f:
#         for linia in f:
#             fragment.append(int(linia.strip()))
#             if len(fragment) == rozmiar_fragmentu:
#                 for num in fragment:
#                     if counter1[num] > 0:
#                         wynik.append(num)
#                         counter1[num] -= 1
#                 fragment = []
#         for num in fragment:
#             if counter1[num] > 0:
#                 wynik.append(num)
#                 counter1[num] -= 1
#     return wynik
