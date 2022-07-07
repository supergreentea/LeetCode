class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        
        # O(n) time complexity, O(n^2) space 
        @cache
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start = 0, partition = []):
            if start == len(s):
                output.append(partition.copy())
                return
            
            for i in range(start, len(s)):
                if is_palindrome(start, i):
                    partition.append(s[start : i + 1])
                    backtrack(i + 1, partition)
                    partition.pop()
        
        backtrack()
        return output