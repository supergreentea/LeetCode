class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        
        def quickselect(nums, l, r, k) :
            if l == r:
                return nums[l]
            pi = partition(nums, l, r)
            if k - 1 < pi:
                return quickselect(nums, l, pi - 1, k)
            elif k - 1 > pi:
                return quickselect(nums, pi + 1, r, k)
            return nums[k - 1]
        
        def partition(nums, l, r):
            i = l
            for j in range(l, r):
                if count[nums[j]] > count[nums[r]]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i
        
        unique = list(count.keys())
        quickselect(unique, 0, len(unique) - 1, k)
        return unique[:k]