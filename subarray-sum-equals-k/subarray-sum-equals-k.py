class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = { 0 : 1 }
        ans = 0
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sums:
                ans += prefix_sums[prefix_sum - k]
            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
        
        return ans