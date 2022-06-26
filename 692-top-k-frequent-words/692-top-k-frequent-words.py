class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        buckets = [[] for _ in range(len(words) + 1)]
        
        for word, count in counts.items():
            buckets[count].append(word)
            
        for bucket in buckets:
            bucket.sort()
        
        output = []
        for i in range(len(words), -1 , -1):
            for word in buckets[i]:
                output.append(word)
                if len(output) == k:
                    return output
                
        return output