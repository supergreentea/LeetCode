class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        
        used = ['0'] * len(nums)
        
        memo = {}
        
        def backtrack(index, subsets_formed, current_sum):
            if current_sum > target_sum:
                return False
            if subsets_formed == k - 1:
                return True
            
            memo_string = ''.join(used)
            
            if memo_string in memo:
                return memo[memo_string]
            
            if current_sum == target_sum:
                memo[memo_string] = backtrack(0, subsets_formed + 1, 0)
                return memo[memo_string]
            
            for i in range(index, len(nums)):
                if used[i] == '0':
                    used[i] = '1'
                    if backtrack(i + 1, subsets_formed, current_sum + nums[i]):
                        return True
                    used[i] = '0'
            
            memo[memo_string] = False
            return False
        
        return backtrack(0, 0, 0)