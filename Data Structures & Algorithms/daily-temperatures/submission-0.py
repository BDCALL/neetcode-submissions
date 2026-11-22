class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for index, temp in enumerate (temperatures):
            while stack and temperatures[stack[-1]] < temp:
                i = stack.pop()
                # index, value
                result.append((i,index-i))
            stack.append(index)
        if stack:
            for index in stack:
                result.append([index,0])
        return [i for j,i in sorted(result, key = lambda x : x[0])]