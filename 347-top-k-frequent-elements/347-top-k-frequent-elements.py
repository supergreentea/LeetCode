class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        frequencies = Counter(nums)
        for num, freq in frequencies.items():
            buckets[freq].append(num)
        
        output = []
        for i in range(len(nums), -1 , -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output