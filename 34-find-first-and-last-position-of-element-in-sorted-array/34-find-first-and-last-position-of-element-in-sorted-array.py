class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def get_first():
            l, r = 0, len(nums) - 1
            first = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    first = m
                    r = m - 1
            return first
        
        def get_last():
            l, r = 0, len(nums) - 1
            last = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    last = m
                    l = m + 1
            return last
        
        return [get_first(), get_last()]