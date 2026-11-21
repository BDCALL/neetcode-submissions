from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        dic = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            dic[c] += 1
        have, need = 0, len(dic)
        l = 0
        best_l = 0
        best_len = float("inf")
        
        
        for r in range (len(s)):
            c = s[r]
            window[c] += 1
            if c in dic and window[c] == dic[c]:
                have += 1         
            while have == need:
                if r-l+1 < best_len:
                    best_len = r-l+1
                    best_l = l
                window[s[l]] -= 1
                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    have -= 1
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]

        

        