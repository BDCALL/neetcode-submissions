class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        string = ""
        # start : 0 0 0 1
        # end : 0 1 3 4
        # "" "z" "zyz"
        # l : 0 1 3
        # zxyz
        for c in s:
            if c not in string:
                string += c
                end += 1
            else:
                while s[start]!=c:
                    start += 1
                start += 1
                end += 1
                string = s[start: end]
            longest = max(longest, len(string))
        return longest


