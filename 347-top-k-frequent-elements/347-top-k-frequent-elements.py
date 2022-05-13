class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        res = []
        for n, c in count.items():
            buckets[c].append(n)
        for i in range(len(nums), -1, - 1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res