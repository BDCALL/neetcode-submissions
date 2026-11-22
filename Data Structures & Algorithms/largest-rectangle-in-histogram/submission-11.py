class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            # Storing index and height
            start = index
            while stack and height < stack[-1][1]:
                # The bar is blocked thus calculate that bars max area
                i, h = stack.pop()
                max_area = max(max_area, h * (index-i))
                # We can extend the current bar back to the bars which has higher height
                start = i
            stack.append([start, height])
        for index, height in stack:
            max_area = max(max_area, height * (len(heights)-index))
        return max_area
        