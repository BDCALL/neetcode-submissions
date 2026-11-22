class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temp in enumerate (temperatures):
            while stack and temperatures[stack[-1]] < temp:
                i = stack.pop()
                # index, value
                result[i] = index-i
            stack.append(index)
        if stack:
            for index in stack:
                result[index] = 0
        return result