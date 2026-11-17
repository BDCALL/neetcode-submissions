class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range (len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        # 1 2 4 6
        # 1 1 2 8
        # 1 2 8 48
        suffix = 1
        for j in range (len(nums)-1,-1,-1):
            answer[j] *= suffix
            suffix *= nums[j]
        # 8 2 1 1
        # 6 4 2 1
        # 8 12 24 48
        # 6 24 48 48
        return answer
