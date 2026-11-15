from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = [[] for _ in range (len(nums)+1)]
        for key, v in count.items():
            result[v].append(key)
        final_result = []
        for j in range (len(result)-1, 0, -1):
            for num in result[j]:
                final_result.append(num)
                if len(final_result) == k:
                    return final_result

        return final_result