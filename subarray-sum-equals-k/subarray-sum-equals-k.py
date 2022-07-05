class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = { 0: 1 }
        ans = 0
        prefix = 0
        
        for num in nums:
            prefix += num
            complement = prefix - k
            if complement in prefixes:
                ans += prefixes[complement]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
        
        return ans