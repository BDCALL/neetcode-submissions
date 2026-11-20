from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dic = defaultdict(int)
        most = (0)
        longest = 0
        for index, char in enumerate (s):
            dic[char] += 1
            if dic[char] > most:
                most = dic[char]
            while (index - l + 1) - most > k:
                dic[s[l]] -= 1
                l += 1
            longest = max(longest, index-l+1)
        return longest
            



        