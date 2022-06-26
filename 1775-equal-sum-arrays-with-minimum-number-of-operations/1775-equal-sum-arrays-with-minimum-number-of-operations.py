class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        
        if sum1 == sum2:
            return 0
        
        larger_array, smaller_array = nums1, nums2
        
        if sum2 > sum1:
            larger_array, smaller_array = nums2, nums1
        
        sum_diff = abs(sum1 - sum2)
        
        # deltas: max we can decrease in larger array and max we can increase in smaller array to get diff closer to 0
        deltas_in_smaller_array = [6 - num for num in smaller_array]
        deltas_in_larger_array = [num - 1 for num in larger_array]
        
        deltas = deltas_in_smaller_array + deltas_in_larger_array
        deltas.sort(reverse = True)
        
        count = 0
        target_diff = sum_diff
        
        for i in range(len(deltas)):
            target_diff -= deltas[i]
            count += 1
            if target_diff <= 0:
                return count
        
        return -1
        
        
        
        