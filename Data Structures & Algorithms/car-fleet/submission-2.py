class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0])

        for car in cars:
            time = float((target - car[0]) / car[1])
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)
    

