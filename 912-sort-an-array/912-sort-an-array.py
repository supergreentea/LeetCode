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
            for j in range(i, r):
                if nums[j] < nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        quicksort(nums, 0, len(nums) - 1)
        return nums