class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lewy, prawy = 0, len(numbers)-1

        while lewy <= prawy:
            print(numbers[lewy], numbers[prawy])
            suma = numbers[lewy] + numbers[prawy]
            if suma == target:
                return [lewy+1, prawy+1]
            elif suma > target:
                prawy -= 1
            else:
                lewy += 1
             



        