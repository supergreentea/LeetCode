class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        frequencies = Counter(arr)
        nums = list(frequencies.keys())
        
        def quickselect(l, r):
            if l == r:
                return nums[l]
            pi = partition(l, r)
            if k - 1 < pi:
                return quickselect(l, pi - 1)
            elif k - 1 > pi:
                return quickselect(pi + 1, r)
            return nums[k - 1]
        
        def partition(l, r):
            p = randint(l, r)
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if frequencies[nums[j]] > frequencies[nums[r]]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        quickselect(0, len(nums) - 1)
        return nums[:k]
        
        
            