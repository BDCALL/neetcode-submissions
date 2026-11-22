class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            # answer on the right
            if  nums[r] < nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid 
        
        return nums[l]
            
        # 3,4,5,6,1,2
        # l = 0 (3) r = 5 (2)
        # mid = 2 (5)
        # l= 3 (6) r =  5 (2)
        # mid = 4 (1)
        # l= 4 r = 5
        # mid = 4

