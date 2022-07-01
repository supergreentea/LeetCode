class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        used = ['0'] * len(nums)
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        memo = {}
        
        def backtrack(index, count, current_sum):
            if count == k - 1:
                return True
            if current_sum > target_sum:
                return False
            
            memo_string = ''.join(used)
            
            if memo_string in memo:
                return memo[memo_string]
            
            if current_sum == target_sum:
                memo[memo_string] = backtrack(0, count + 1, 0)
                return memo[memo_string]
            
            for i in range(index, len(nums)):
                if used[i] == '0':
                    used[i] = '1'
                    if backtrack(i + 1, count, current_sum + nums[i]):
                        return True
                    used[i] = '0'
            
            memo[memo_string] = False
            return False
        
        return backtrack(0, 0, 0)
            