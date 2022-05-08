class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        Count = Counter(nums)
        
        for key, val in Count.items():
            buckets[val].append(key)
        
        res = []
        
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []
        