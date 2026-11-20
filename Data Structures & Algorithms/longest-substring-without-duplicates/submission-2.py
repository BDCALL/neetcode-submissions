class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        longest = 0
        for i, v in enumerate(s):
            if v  in last_seen and last_seen[v] >= l:
                l = last_seen[v] + 1
            last_seen[v] = i
            longest = max(longest, i-l+1)
        return longest


