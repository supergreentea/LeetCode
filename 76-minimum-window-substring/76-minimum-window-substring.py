class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not s:
            return ""
        
        s_counter, t_counter = defaultdict(int), defaultdict(int)
        
        for c in t:
            t_counter[c] += 1
        
        # values chosen so that if valid window substring is found with smaller length, we can update these values
        # if ans_right remains len(s), then we know no valid substring window was found
        ans_left, ans_right = 0, len(s)
        
        have, need = 0, len(t_counter)
        
        window_left = 0
        for window_right in range(len(s)):
            cur_char = s[window_right]
            if cur_char in t_counter:
                s_counter[cur_char] += 1
                if s_counter[cur_char] == t_counter[cur_char]:
                    have += 1
                    while have == need:
                        if ans_right - ans_left > window_right - window_left:
                            ans_left, ans_right = window_left, window_right
                        front_char = s[window_left]
                        s_counter[front_char] -= 1
                        if front_char in t_counter and s_counter[front_char] == t_counter[front_char] - 1:
                            have -= 1
                        window_left += 1
                        
        if ans_right == len(s):
            return ""
        
        return s[ans_left : ans_right + 1]
                    
        
        