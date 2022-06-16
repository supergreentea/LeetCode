"""
Strategy:

Use a backtracking function
used = set()
backtrack(index, subsets_formed, subset_sum)

index: index of value in array we are considering
subsets_formed: count of subsets with target sum we have formed so far in backtracking path
subset_sum: sum of elements used in current backtracking path

if we have already formed k - 1 subsets with sum == target, then the remaining unused elements must also sum to target, so we can return True
when our subset sum exceeds the target, we can return false
if our subset sum is target, we can increment subsets_formed and backtrack from beginning with backtrack(0, subsets_formed + 1, 0) 


for i in range(index, len(nums)):
    if element at i is not used:
        mark it as used
        if backtrack(index + 1, subsets_formed, subset_sum):
            return True
        mark element at i as unused so i can be used in other backtracking paths
if we were not able to find a successful backtracking path to form k sets, we return False

"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        used = ['0'] * len(nums)
        memo = {}
        
        def backtrack(index, subsets_formed, subset_sum):
            if subsets_formed == k - 1:
                return True
            if subset_sum > target_sum:
                return False
            memo_string = ''.join(used)
            if memo_string in memo:
                return memo[memo_string]
            if subset_sum == target_sum:
                memo[memo_string] = backtrack(0, subsets_formed + 1, 0)
                return memo[memo_string]
            for i in range(index, len(nums)):
                if used[i] == '0':
                    used[i] = '1'
                    if backtrack(index + 1, subsets_formed, subset_sum + nums[i]):
                        return True
                    used[i] = '0'
            memo[memo_string] = False
            return False
        
        return backtrack(0, 0, 0)
            