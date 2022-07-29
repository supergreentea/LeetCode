class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque([])
        
        for c in s:
            if stack and stack[-1][0] == c:
                char, count = stack.pop()
                count += 1
                if count >= k:
                    count -= k
                if count == 0:
                    continue
                else:
                    stack.append((char, count))
            else:
                stack.append((c, 1))
        
        res = deque([])
        while stack:
            char, count = stack.pop()
            for _ in range(count):
                res.appendleft(char)
        
        return ''.join(res)
                    
            