class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        Count = Counter(nums)
        for num, count in Count.items():
            buckets[count].append(num)
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []