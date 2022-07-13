"""
Binary search.

1. We have two pointers left and right starting at 0 and len(nums) - 1
2. while left <= right:
        get middle
        if middle is target, return middle
        if left half is sorted and target in left half, search left half else search right half
        otherwise if right half is sorted and target in right half, search right half else search left half

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            
            # left to middle is sorted
            if nums[middle] >= nums[left]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else: # middle to right is sorted
                if target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1