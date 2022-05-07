class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def quickselect(unique, l, r, k, Dict):
            if l == r:
                return unique[l]
            pi = partition(unique, l, r, Dict)
            if pi == k - 1:
                return [pi]
            elif k - 1 < pi:
                return quickselect(unique, l, pi - 1, k, Dict)
            return quickselect(unique, pi + 1, r, k, Dict)
            
        def partition(unique, l, r, Dict):
            p = randint(l, r)
            unique[r], unique[p] = unique[p], unique[r]
            i = l
            for j in range(l, r):
                if Dict[unique[j]] > Dict[unique[r]]:
                    unique[j], unique[i] = unique[i], unique[j]
                    i += 1
            unique[i], unique[r] = unique[r], unique[i]
            return i
        
        Dict = Counter(nums)
        
        print(Dict)
        
        unique = list(Dict.keys())
        
        quickselect(unique, 0, len(unique) - 1, k, Dict)
        
        print(unique)
        
        return unique[:k]