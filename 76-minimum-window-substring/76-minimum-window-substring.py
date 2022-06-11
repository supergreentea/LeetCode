class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        l = r = 0
        counter = Counter()
        start, end = 0, len(s)
        while r < len(s):
            counter[s[r]] += 1
            while counter & t_counter == t_counter:
                if r - l < end - start:
                    start, end = l, r
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1
            r += 1
        if end == len(s):
            return ""
        return s[start : end + 1]
                
            
            