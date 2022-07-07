class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        
        @cache
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def backtrack(start = 0, partition = []):
            if start >= len(s):
                output.append(partition.copy())
                return
            
            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    partition.append(s[start : i + 1])
                    backtrack(i + 1, partition)
                    partition.pop()
        
        backtrack()
        return output
                