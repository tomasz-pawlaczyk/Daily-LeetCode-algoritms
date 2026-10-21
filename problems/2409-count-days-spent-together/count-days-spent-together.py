# Używając sum prefiksowych
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in days_month:
            prefix.append(prefix[-1] + d)

        def day_of_year(date: str) -> int:
            return prefix[int(date[:2]) - 1] + int(date[3:])

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))
        return max(0, end - start + 1)




# class Solution:
#     def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
#         days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#         if int(arriveAlice[:2]) < int(arriveBob[:2]):
#             start = arriveBob
#         elif int(arriveAlice[:2]) > int(arriveBob[:2]):
#             start = arriveAlice
#         else:
#             if int(arriveAlice[3:]) < int(arriveBob[3:]):
#                 start = arriveBob
#             else:
#                 start = arriveAlice

#         if int(leaveAlice[:2]) > int(leaveBob[:2]):
#             end = leaveBob
#         elif int(leaveAlice[:2]) < int(leaveBob[:2]):
#             end = leaveAlice
#         else:
#             if int(leaveAlice[3:]) > int(leaveBob[3:]):
#                 end = leaveBob
#             else:
#                 end = leaveAlice

#         s_month = int(start[:2])
#         s_day = int(start[3:])
#         e_month = int(end[:2])
#         e_day = int(end[3:])
#         result = 0
#         for i in range(s_month, e_month+1):
#             result += days_month[i-1]
#         result -= s_day + (days_month[e_month-1] - e_day)
#         return max(result + 1, 0)


        