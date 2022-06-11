class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        n = len(nums)
        taken = ['0'] * n
        memo = {}
        
        def backtrack(index, count, curr_sum):
            if count == k - 1:
                return True
            if curr_sum > target_sum:
                return False
            taken_str = ''.join(taken)
            if taken_str in memo:
                return memo[taken_str]
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]
            for i in range(index, n):
                if taken[i] == '0':
                    taken[i] = '1'
                    if backtrack(index + 1, count, curr_sum + nums[i]):
                        return True
                    taken[i] = '0'
            memo[taken_str] = False
            return False
        
        return backtrack(0, 0, 0)