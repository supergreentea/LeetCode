class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l < r:
            Sum = nums[l] + nums[r]
            if Sum < target:
                l += 1
            elif Sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        
        return []