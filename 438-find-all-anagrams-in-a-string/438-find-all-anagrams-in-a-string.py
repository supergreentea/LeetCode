class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        keys = len(p_counter)
        formed = 0
        s_counter = defaultdict(int)
        window_left = 0
        ans = []
        for window_right in range(len(s)):
            cur_char = s[window_right]
            
            if window_right - window_left + 1 > len(p):
                char_left = s[window_left]
                if s_counter[char_left] == p_counter[char_left]:
                    formed -= 1
                s_counter[char_left] -= 1
                window_left += 1
                
            if s_counter[cur_char] == p_counter[cur_char] - 1:
                formed += 1
                if formed == keys:
                    ans.append(window_left)
                    
            s_counter[cur_char] += 1
        return ans
            
                