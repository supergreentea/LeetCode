class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(l, r):
            if l < r:
                pi = partition(l, r)
                quicksort(l, pi - 1)
                quicksort(pi + 1, r)
        
        def partition(l, r):
            p = randint(l, r)
            nums[r], nums[p] = nums[p], nums[r]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        quicksort(0, len(nums) - 1)