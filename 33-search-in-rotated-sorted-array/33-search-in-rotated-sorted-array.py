class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # l to m is strictly ascending (before rotation index)
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # m to r is strictly ascending
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1