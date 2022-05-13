class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(nums, l, r):
            if l < r:
                pi = partition(nums, l, r)
                quicksort(nums, l, pi - 1)
                quicksort(nums, pi + 1, r)
        
        def partition(nums, l, r):
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        quicksort(nums, 0, len(nums) - 1)
        return nums