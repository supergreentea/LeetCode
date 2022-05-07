class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k)
        
        
    def quickselect(self, nums, low, high, k):
        if low == high:
            return nums[low]
        pi = self.partition(nums, low, high)
        if k - 1 == pi:
            return nums[k - 1]
        elif k - 1 < pi:
            return self.quickselect(nums, low, pi - 1, k)
        return self.quickselect(nums, pi + 1, high, k)
    
    def partition(self, nums, low, high):
        pivotIndex = randint(low, high)
        pivot = nums[pivotIndex]
        self.swap(nums, pivotIndex, high)
        
        i = low - 1
        for j in range(low, high):
            if nums[j] > pivot:
                i += 1
                self.swap(nums, i, j)
        self.swap(nums, i + 1, high)
        return i + 1
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp