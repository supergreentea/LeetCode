class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for num, freq in count.items():
            buckets[freq].append(num)
        output = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output