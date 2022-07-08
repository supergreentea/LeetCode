class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                char, count = stack.pop()
                if count + 1 == k:
                    continue
                stack.append((char, count + 1))
            else:
                stack.append((c, 1))
        
        res = ""
        while stack:
            char, count = stack.pop()
            res = char * count + res
        
        return res
            
        
        
            
            
                
                    
            