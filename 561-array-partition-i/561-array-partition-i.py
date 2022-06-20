class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        counts = [0] * 20001
        for num in nums:
            counts[num + 10000] += 1
        i = 0
        for j in range(20001):
            while counts[j] > 0:
                nums[i] = j - 10000
                i += 1
                counts[j] -= 1
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i + 1])
        return max_sum