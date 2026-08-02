class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(0, len(temperatures)):
            counter = 0
            found = False
            for j in range(i+1, len(temperatures)):
                counter += 1
                if (temperatures[j] > temperatures[i]):
                    result.append(counter)
                    found = True
                    break
            if not found:
                result.append(0)
        return result
