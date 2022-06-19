class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        key_value_pairs = list(counts.items())
        
        key_value_pairs.sort(key = lambda item : item[1], reverse = True)
        
        return [x[0] for x in key_value_pairs[:k]]