class Solution:
    def minDeletions(self, s: str) -> int:
        delete_count = 0
        frequencies = [0] * 26
        for c in s:
            frequencies[ord(c) - ord('a')] += 1
        frequencies.sort(reverse=True)
        max_allowed = len(s)
        for frequency in frequencies:
            if frequency > max_allowed:
                delete_count += frequency - max_allowed
                frequency = max_allowed
            max_allowed = max(0, frequency - 1)
        return delete_count