class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % k != 0:
            return False
        used = ['0'] * n
        target = total // k
        memo = {}
        
        def backtrack(index, count, curr_sum):
            used_str = ''.join(used)
            if count == k - 1:
                return True
            if curr_sum > target:
                return False
            if used_str in memo:
                return memo[used_str]
            if curr_sum == target:
                memo[used_str] = backtrack(0, count + 1, 0)
                return memo[used_str]
            for i in range(index, n):
                if used[i] == '0':
                    used[i] = '1'
                    if backtrack(index + 1, count, curr_sum + nums[i]):
                        return True
                    used[i] = '0'
            memo[used_str] = False
            return False
        
        return backtrack(0, 0, 0)