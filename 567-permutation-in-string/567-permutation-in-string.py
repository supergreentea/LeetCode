class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        n = len(s2)
        for i in range(0, len(s2) - len(s1) + 1):
            if s2[i] in s1_counter:
                if s1_counter == Counter(s2[i : i + len(s1)]):
                    return True
        return False