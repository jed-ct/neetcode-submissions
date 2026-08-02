class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue
            while stack and temp > stack[-1][0]:
                popped_pair = stack.pop()
                result[popped_pair[1]] = i - popped_pair[1]
            stack.append((temp, i))
        return result
            
            

        
