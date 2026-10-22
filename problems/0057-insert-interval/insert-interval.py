class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # 1. przedziały całkiem przed nowym
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. przedziały nachodzące na nowy: scalamy
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # 3. przedziały całkiem za nowym
        result.extend(intervals[i:])
        return result


# Moje 
# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
#         result = []

#         i = 0
#         while i < len(intervals):
#             current = intervals[i]
#             if newInterval[1] < current[0]:
#                 result.append(newInterval)
#                 result.extend(intervals[i:])
#                 return result
            
#             elif newInterval[0] > current[1]:
#                 result.append(current)
            
#             elif newInterval[0] <= current[1]: 
#                 if newInterval[1] < current[1]:
#                     result.append([min(newInterval[0], current[0]), current[1]])
#                     result.extend(intervals[i+1:])
#                     return result

#                 elif newInterval[1] >= current[1]:
#                     start = min(newInterval[0], current[0])
#                     end = newInterval[1]
#                     while i < len(intervals) and newInterval[1] >= intervals[i][0]:
#                         end = max(newInterval[1], intervals[i][1])
#                         i += 1
                        
#                     result.append([start, end])
#                     result.extend(intervals[i:])
#                     return result

#             i += 1
#         result.append(newInterval)
#         return result




