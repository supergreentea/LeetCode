class Solution:
    def frequencySort(self, s: str) -> str:
        # O(n) space and O(n) time for construction of counter
        counter = Counter(s)
        max_freq = max(counter.values())
        buckets = [[] for _ in range(max_freq + 1)]
        
        # O(n) space and O(n) time for construction of counter
        counter = Counter(s)
        
        for item, count in counter.items():
            buckets[count].append(item)
        
        res = []
        
        # O(n) appends
        for count in range(len(buckets) - 1, -1, - 1):
            for item in buckets[count]:
                res.append(item * count)
        
        return ''.join(res)