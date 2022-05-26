class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
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
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        quicksort(0, len(nums) - 1)
        return nums
            