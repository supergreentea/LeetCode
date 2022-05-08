class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        
        def quickselect(unique, l, r, k):
            if l == r:
                return unique[l]
            pi = partition(unique, l, r)
            if pi == k - 1:
                return unique[k - 1]
            elif k - 1 < pi:
                return quickselect(unique, l, pi - 1, k)
            return quickselect(unique, pi + 1, r, k)
        
        def partition(unique, l, r):
            i = l
            for j in range(l, r):
                if count[unique[j]] > count[unique[r]]:
                    unique[j], unique[i] = unique[i], unique[j]
                    i += 1
            unique[r], unique[i] = unique[i], unique[r]
            return i
        
        quickselect(unique, 0, len(unique) - 1, k)
        
        return unique[:k]