class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()

        j = 0   # najbliższy grzejnik dla katualnie rozpatrywanego domu
        promien = 0
        for house in houses:
            while j < len(heaters)-1 and abs(heaters[j+1] - house) <= abs(heaters[j] - house):
                j += 1
            promien = max(promien, abs(heaters[j] - house))
        return promien









# class Solution:
#     def findRadius(self, houses: list[int], heaters: list[int]) -> int:
#         result = 0
#         for i in range(len(houses)):
#             house = houses[i]

#             min_distance = float('inf')
#             for heater in heaters:
#                 distance = abs(house - heater)
#                 if distance < min_distance:
#                     min_distance = distance
#                 if distance < result:
#                     break
#             i += min_distance
#             if min_distance > result:
#                 result = min_distance
            
#         return result