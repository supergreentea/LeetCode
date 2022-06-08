class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % k != 0:
            return False
        memo = {}
        taken = ['0'] * n
        target = total // k
        
        def backtrack(index, count, curr_sum):
            taken_str = ''.join(taken)
            if count == k - 1:
                return True
            if curr_sum > target:
                return False
            if taken_str in memo:
                return memo[taken_str]
            if curr_sum == target:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            for j in range(index, n):
                if taken[j] == '0':
                    taken[j] = '1'
                    if backtrack(index + 1, count, curr_sum + nums[j]):
                        return True
                    taken[j] = '0'
            memo[taken_str] = False
            return memo[taken_str]
        
        return backtrack(0, 0, 0)
            