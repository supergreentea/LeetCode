class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            # array is sorted in increasing order in left half
            if nums[middle] >= nums[left]:
                
                # target lies within bounds of left half
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # array is sorted in increasing order in right half
            else:
                
                # target within bounds of right half
                if target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            
        return -1