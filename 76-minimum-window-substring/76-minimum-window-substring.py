class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        """
        Strategy:
        Use a sliding window approach.
        Use two pointers, l and r both starting at 0.
        Extend r until t is included in window.
        As long as t is included in window, we move l to decrease window until t is no longer included in window; we move r again until t is included again.
        We update the pointers for the minimum window substring while this is happening.
        We can use a Counter to keep track of frequency of characters in window.
        We can use a Counter with the frequency of characters in t for comparison.
        If the intersection of the two counters is the counter for t, then we know t is in that window.
        We can return return the min window substring using the pointers we kept track of.
        """
        l = r = 0
        ans_l, ans_r = 0, len(s)
        t_counter = Counter(t)
        window_counter = Counter()
        while r < len(s):
            window_counter[s[r]] += 1
            while t_counter & window_counter == t_counter:
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r
                window_counter[s[l]] -= 1
                if window_counter[s[l]] == 0:
                    del window_counter[s[l]]
                l += 1
            r += 1
        if ans_r == len(s):
            return ""
        return s[ans_l:ans_r + 1]