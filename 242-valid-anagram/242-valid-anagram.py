class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Dict = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            Dict[s[i]] += 1
            Dict[t[i]] -= 1
        for count in Dict.values():
            if count != 0:
                return False
        return True