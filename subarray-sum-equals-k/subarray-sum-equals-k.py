class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = { 0 : 1 }
        count = 0
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            
            count += prefixes.get(complement, 0)
            prefixes[prefix_sum] = prefixes.get(prefix_sum, 0) + 1
        
        return count
        