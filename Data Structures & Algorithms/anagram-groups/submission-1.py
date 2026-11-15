from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                place = ord(c) - ord('a')
                count[place] += 1
            group[tuple(count)].append(s)
        return list(group.values())
