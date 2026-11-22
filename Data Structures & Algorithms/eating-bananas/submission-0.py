import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            hours = 0
            rate = l + (r-l) // 2
            for pile in piles:
                hours += math.ceil(pile / rate)
            # Need eat faster, higher rate
            if hours > h:
                l = rate + 1
            # Eatting too slow
            else:
                r = rate-1
        return l



        