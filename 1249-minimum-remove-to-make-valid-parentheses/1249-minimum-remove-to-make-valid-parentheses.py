class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append((char, i))
            elif char == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((char, i))
        to_remove = set()
        while stack:
            to_remove.add(stack.pop()[1])
        res = []
        for i in range(len(s)):
            if i not in to_remove:
                res.append(s[i])
        
        return ''.join(res)