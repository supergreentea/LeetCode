class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        shortest = 51
        
        for start in range(N):
            for end in range(start, N):
                orSum = 0
                for i in range(start, end + 1):
                    orSum |= nums[i]
                    if orSum >= k:
                        shortest = min(shortest, end - start + 1)
        
        return shortest if shortest != 51 else -1