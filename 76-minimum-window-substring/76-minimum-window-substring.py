"""
Time complexity: O(|S| + |T|) where |S| and |T| represent the lengths of strings S and T. 
- We need to iterate through all elements of T to form the dictionary.
- We need to iterate through all the elements of S at most 2 times, once with left pointer and once with right pointer.
Space complexity: O(|S| +|T|)
- The dictionary sizes scale with the number of unique elements in S and T, which are at most |S| and |T|
"""

"""
Strategy:
Sliding window algorithm:
    - use two pointers, l and r (denoting the left side and right sides of the sliding window)
    - move r until we know the window has all the characters in t. update our result indices (indices indicating start and end of substring answer)
    - when window has all characters in t, move left pointer to shrink window until that condition is false, then expand window again by moving r 
    - to find new substring fulfilling condition

Maintain two dictionaries
window_count : frequency of characters in current window
t_count: frequency of characters in string t
"""


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
        
        
        