class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = ['0'] * len(nums)
        memo = {}
        
        def backtrack(i, k, subset_sum):
            taken_string = ''.join(used)
            if taken_string in memo:
                return memo[taken_string]
            if k == 0:
                return True
            if subset_sum == target:
                memo[taken_string] = backtrack(0, k - 1, 0)
                return memo[taken_string] 
            
            for j in range(i, len(nums)):
                if used[j] == '1' or nums[j] + subset_sum > target:
                    continue
                used[j] = '1'
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = '0'
            
            memo[taken_string] = False
            return memo[taken_string]
        
        return backtrack(0, k, 0)
                