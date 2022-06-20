class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = [0] * 100001
        for num in nums:
            counts[num + 50000] += 1
        
        num_items_before = 0
        for i in range(100001):
            count = counts[i]
            counts[i] = num_items_before
            num_items_before += count
        
        sorted_array = [0] * len(nums)
        
        for num in nums:
            sorted_array[counts[num + 50000]] = num
            counts[num + 50000] += 1
        
        return sorted_array