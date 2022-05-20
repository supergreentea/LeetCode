class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        res = []
        
        for key, value in count.items():
            buckets[value].append(key)
        
        for i in range(len(nums), -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []