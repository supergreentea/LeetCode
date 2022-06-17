class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        elements = list(frequency.keys())
        
        def quickselect(l, r):
            if l == r:
                return elements[r]
            
            pi = partition(l, r)
            
            if k - 1 < pi:
                return quickselect(l, pi - 1)
            elif k - 1 > pi:
                return quickselect(pi + 1, r)
            else:
                return elements[k - 1]
            
        def partition(l, r):
            p = randint(l, r)
            nums[r], nums[p] = nums[p], nums[r]
            i = l
            for j in range(l, r):
                if frequency[elements[j]] > frequency[elements[r]]:
                    elements[j], elements[i] = elements[i], elements[j]
                    i += 1
            elements[i], elements[r] = elements[r], elements[i]
            return i
        
        quickselect(0, len(elements) - 1)
        return elements[:k]
            