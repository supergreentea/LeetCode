class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        memo = {}
        
        def is_palindrome(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            while l < r:
                if s[l] != s[r]:
                    memo[(l, r)] = False
                    return False
                l, r = l + 1, r - 1
            memo[(l, r)] = True
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
                