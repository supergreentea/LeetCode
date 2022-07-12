class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        
        window_front = 0
        for window_end in range(len(s)):
            current_char = s[window_end]
            while current_char in seen:
                seen.remove(s[window_front])
                window_front += 1
            seen.add(current_char)
            window_length = window_end - window_front + 1
            max_length = max(max_length, window_length)
        
        return max_length