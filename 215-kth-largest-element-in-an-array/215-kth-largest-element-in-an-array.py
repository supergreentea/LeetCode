class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(nums, l, r, k):
            if l == r:
                return nums[r]
            pi = partition(nums, l, r)
            if pi == k - 1:
                return nums[pi]
            elif k - 1 < pi:
                return quickselect(nums, l, pi - 1, k)
            return quickselect(nums, pi + 1, r, k)
        
        def partition(nums, l, r):
            i = l
            for j in range(l, r):
                if nums[j] > nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        return quickselect(nums, 0, len(nums) - 1, k)