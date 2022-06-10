class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        unique = list(frequencies.keys())
        
        def quickselect(l, r, k):
            if l == r:
                return unique[l]
            pi = partition(l, r)
            
            if k - 1 < pi:
                return quickselect(l, pi - 1, k)
            elif k - 1 > pi:
                return quickselect(pi + 1, r, k)
            else:
                return unique[k - 1]
        
        def partition(l, r):
            p = randint(l, r)
            unique[p], unique[r] = unique[r], unique[p]
            i = l
            for j in range(l, r):
                if frequencies[unique[j]] > frequencies[unique[r]]:
                    unique[j], unique[i] = unique[i], unique[j]
                    i += 1
            unique[i], unique[r] = unique[r], unique[i]
            return i
        
        quickselect(0, len(unique) - 1, k)
        return unique[:k]