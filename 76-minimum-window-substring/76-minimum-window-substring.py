class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or s == "":
            return ""
        
        window_count, t_count = defaultdict(int), defaultdict(int)
        
        for c in t:
            t_count[c] += 1
        
        have, need = 0, len(t_count)
        
        res_left, res_right = 0, len(s)
        
        l = 0
        for r in range(len(s)):
            window_count[s[r]] += 1
            if s[r] in t_count:
                if window_count[s[r]] == t_count[s[r]]:
                    have += 1
                    while have == need:
                        if r - l < res_right - res_left:
                            res_left, res_right = l, r
                        window_count[s[l]] -= 1
                        if s[l] in t_count and window_count[s[l]] == t_count[s[l]] - 1:
                            have -= 1
                        l += 1
        if res_right == len(s):
            return ""
        return s[res_left : res_right + 1]
        
        
        