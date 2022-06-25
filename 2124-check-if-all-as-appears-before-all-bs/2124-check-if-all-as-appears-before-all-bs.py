class Solution:
    def checkString(self, s: str) -> bool:
        index = 0
        while index < len(s) and s[index] != 'b':
            index += 1
        while index < len(s):
            if s[index] == 'a':
                return False
            index += 1
        return True