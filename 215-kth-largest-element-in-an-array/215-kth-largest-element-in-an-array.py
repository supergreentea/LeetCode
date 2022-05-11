class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(nums, l, r, k):
            if l == r:
                return nums[r]
            pi = partition(nums, l, r)
            if k - 1 == pi:
                return nums[k - 1]
            elif k - 1 < pi:
                return quickselect(nums, l, pi - 1, k)
            return quickselect(nums, pi + 1, r, k)
        
        def partition(nums, l, r):
            i = l - 1
            for j in range(l, len(nums)):
                if nums[j] > nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[r], nums[i + 1] = nums[i + 1], nums[r]
            return i + 1
        
        return quickselect(nums, 0, len(nums) - 1, k)
        