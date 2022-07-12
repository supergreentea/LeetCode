class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_counter, t_counter = defaultdict(int), Counter(t)
        
        ans_l, ans_r = 0, len(s)
        
        l = 0
        have, need = 0, len(t_counter)
        
        for r in range(len(s)):
            s_counter[s[r]] += 1
            if s_counter[s[r]] == t_counter[s[r]]:
                have += 1
                while have == need:
                    if r - l < ans_r - ans_l:
                        ans_l, ans_r = l, r
                    s_counter[s[l]] -= 1
                    if s_counter[s[l]] == t_counter[s[l]] - 1:
                        have -= 1
                    l += 1
                    
        return s[ans_l : ans_r + 1] if ans_r != len(s) else ""