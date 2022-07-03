class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or diff < 0 and prev_diff >= 0:
                count += 1
                prev_diff = diff
        return count
            
            
            
        
        