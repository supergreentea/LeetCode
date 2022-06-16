class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        # if no rotation return first element
        if nums[0] <= nums[-1]:
            return nums[0]
        
        # binary search (log(N) time complexity):
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m] < nums[m - 1]:
                return nums[m]
            if nums[0] < nums[m]: # left of inflection point, so go right
                l = m + 1
            else:
                r = m - 1 # right of inflection point, so go left
                