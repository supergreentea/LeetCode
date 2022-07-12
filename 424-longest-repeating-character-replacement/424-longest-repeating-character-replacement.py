class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        
        window_front = 0
        for window_end in range(len(s)):
            current_char = s[window_end]
            count[current_char] += 1
            most_frequent = max(count.values())
            while window_end - window_front + 1 - max(count.values()) > k:
                count[s[window_front]] -= 1
                window_front += 1
            ans = max(ans, window_end - window_front + 1)
        
        return ans