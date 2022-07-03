class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for _ in range(5 * 10 ** 5 + 1)]
        counter = Counter(s)
        
        for item, count in counter.items():
            buckets[count].append(item)
        
        res = []
        
        for count in range(len(buckets) - 1, -1, - 1):
            for item in buckets[count]:
                for _ in range(count):
                    res.append(item)
        
        return ''.join(res)