class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        l,r = 0, len(height)-1
        prefix[l], suffix[r] = height[l], height[r]
        while l < len(height):
            if l > 0:
                prefix[l] = max(height[l], prefix[l-1])
                suffix[r] = max(height[r], suffix[r+1])
            l += 1
            r -= 1
        area = 0
        for i in range (len(height)):
            area += min(prefix[i], suffix[i]) - height[i]
        return area
