class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # we know l to m is sorted
            if nums[left] <= nums[mid]:
                # target within left sorted portion
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # m to r is sorted
                # target within right sorted portion
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
                