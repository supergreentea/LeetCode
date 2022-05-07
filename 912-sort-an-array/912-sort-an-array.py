class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(nums, l, r):
            if l < r:
                pi = partition(nums, l, r)
                quicksort(nums, l, pi - 1)
                quicksort(nums, pi + 1, r)
        
        # lomuto's partition algorithm
        def partition(nums, l, r):
            pivotIndex = random.randint(l, r)
            nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex] # place pivot at end of range
            i = l - 1
            for j in range(l, r):
                if nums[j] < nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[r] = nums[r], nums[i + 1]
            return i + 1
        
        quicksort(nums, 0, len(nums) - 1)
        return nums