class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        output = []
        
        def backtrack(index = 0, partition = []):
            if index == len(s):
                output.append(partition.copy())
                return
            for i in range(index, len(s)):
                if is_palindrome(index, i):
                    partition.append(s[index : i + 1])
                    backtrack(i + 1, partition)
                    partition.pop()
        
        backtrack()
        return output
                