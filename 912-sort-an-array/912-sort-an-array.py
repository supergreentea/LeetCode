class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(l, r):
            if l < r:
                p = partition(l, r)
                quicksort(l, p - 1)
                quicksort(p + 1, r)
        
        def partition(l, r):
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        quicksort(0, len(nums) - 1)
        return nums