class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        counts = list(counter.values())
        counts.sort(reverse = True)
        
        deletions = 0
        max_allowed = counts[0]
        for count in counts:
            if count > max_allowed:
                deletions += count - max_allowed
                count = max_allowed
            max_allowed = max(0, count - 1)
        return deletions