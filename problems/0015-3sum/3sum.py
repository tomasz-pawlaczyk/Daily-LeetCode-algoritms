class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1  # trzeba o tym pamiętać
                continue
            lewo, prawo = i+1, len(nums)-1
            while lewo < prawo:
                if lewo == i:
                    lewo += 1
                elif prawo == i:
                    prawo -= 1
                else:
                    suma = nums[i] + nums[lewo] + nums[prawo]
                    if suma == 0:
                        lista = sorted([nums[i], nums[lewo], nums[prawo]])
                        result.append(lista)
                        lewo += 1
                        prawo -= 1
                        while lewo < prawo and nums[lewo] == nums[lewo-1]:
                            lewo += 1
                        while lewo < prawo and nums[prawo] == nums[prawo+1]:
                            prawo -= 1
                    elif suma < 0:
                        lewo += 1
                    else:
                        prawo -= 1
            i += 1
        return result

# Wykorzystaliśmy zablokowanie jednej cyfry co sprowadziło do problemu 2 sum oraz sortowanie i dalsze 2 wskaźniki
# co dało stałą pamięć