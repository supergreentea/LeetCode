class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(l, r):
            if l < r:
                pi = partition(l, r)
                quicksort(l, pi - 1)
                quicksort(pi + 1, r)
            
        
        def partition(l, r):
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        quicksort(0, len(nums) - 1)
        return nums
            