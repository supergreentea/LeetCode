class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(nums, l, r, k):
            if l == r:
                return nums[l]
            
            pi = partition(nums, l, r)
            
            if k - 1 < pi:
                return quickselect(nums, l, pi - 1, k)
            if k - 1 > pi:
                return quickselect(nums, pi + 1, r, k)
            return nums[k - 1]
        
        def partition(nums, l, r):
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            
            i = l
            for j in range(l, r):
                if nums[j] > nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        return quickselect(nums, 0, len(nums) - 1, k)
            
            