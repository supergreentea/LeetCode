class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        count = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_sums:
                count += prefix_sums[cur_sum - k]
            prefix_sums[cur_sum] += 1
        return count