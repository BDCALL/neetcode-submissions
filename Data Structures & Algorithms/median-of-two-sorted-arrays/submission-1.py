class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # A is the shorter one
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = (total + 1) // 2

        l, r = 0, len(A)
        while l <= r:
            # If we take i from A, we take half-i from B
            i = (l+r) // 2
            j = half - i 

            # Handle edge cases
            A_left = A[i-1] if i>0 else float("-inf")
            A_right = A[i] if i< len(A) else float("inf")
            B_left = B[j-1] if j>0 else float("-inf")
            B_right = B[j] if j<len(B) else float("inf")

            # Correct split of the left and right side of the median 
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right))/2
            
            # Took too many from A
            elif A_left > B_right:
                r = i-1
            # Took too less from A
            else:
                l = i+1
            # [1 2 | 3 4]
            # [1 2 3 |  4 5 ]

        