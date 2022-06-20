class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        window_counter = Counter()
        window_left = 0
        completed = 0
        
        for window_right in range(len(s2)):
            cur_char = s2[window_right]
            if not cur_char in s1_counter:
                window_left = window_right + 1
                window_counter = Counter()
                completed = 0
                continue
            window_counter[cur_char] += 1
            if window_counter[cur_char] == s1_counter[cur_char]:
                completed += 1
                if completed == len(s1_counter):
                    return True
            while window_counter[cur_char] > s1_counter[cur_char]:
                left_char = s2[window_left]
                window_counter[left_char] -= 1
                if window_counter[left_char] == s1_counter[left_char] - 1:
                    completed -= 1
                window_left += 1
        
        return False