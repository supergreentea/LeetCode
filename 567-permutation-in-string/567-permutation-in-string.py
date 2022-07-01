class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def matches():
            for i in range(26):
                if s1_count[i] != s2_count[i]:
                    return False
            return True
        
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if matches():
            return True
        
        for i in range(len(s2) - len(s1)):
            s2_count[ord(s2[len(s1) + i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] -= 1
            if matches():
                return True
        
        return False
        
        